#!/usr/bin/env python3
"""Generate a proof-based weekly marketing pack from a GitHub account.

The agent is intentionally draft-only. It reads repository metadata and README
content, ranks suitable projects, writes channel-ready copy, and optionally
creates or updates one rolling GitHub issue in the profile repository.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

API_ROOT = "https://api.github.com"
USER_AGENT = "keepithandy-repo-marketing-agent/0.1"


class GitHubError(RuntimeError):
    """Raised when the GitHub API returns an unexpected response."""


class GitHubClient:
    def __init__(self, token: str | None = None, api_root: str = API_ROOT) -> None:
        self.token = token
        self.api_root = api_root.rstrip("/")

    def request(
        self,
        path: str,
        *,
        method: str = "GET",
        payload: dict[str, Any] | None = None,
        accept: str = "application/vnd.github+json",
        allow_not_found: bool = False,
    ) -> Any:
        url = path if path.startswith("http") else f"{self.api_root}{path}"
        body = None
        headers = {
            "Accept": accept,
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        request = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                if not raw:
                    return None
                if accept.startswith("application/vnd.github.raw"):
                    return raw.decode("utf-8", errors="replace")
                return json.loads(raw.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if allow_not_found and exc.code == 404:
                return None
            detail = exc.read().decode("utf-8", errors="replace")
            raise GitHubError(f"GitHub API {exc.code} for {url}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise GitHubError(f"Unable to reach GitHub API at {url}: {exc.reason}") from exc

    def list_owner_repositories(self, owner: str) -> list[dict[str, Any]]:
        repositories: list[dict[str, Any]] = []
        page = 1
        while True:
            query = urllib.parse.urlencode(
                {
                    "per_page": 100,
                    "page": page,
                    "sort": "pushed",
                    "direction": "desc",
                    "type": "owner",
                }
            )
            batch = self.request(f"/users/{owner}/repos?{query}")
            if not isinstance(batch, list):
                raise GitHubError("Repository response was not a list.")
            repositories.extend(batch)
            if len(batch) < 100:
                break
            page += 1
        return repositories

    def get_readme(self, full_name: str) -> str:
        result = self.request(
            f"/repos/{full_name}/readme",
            accept="application/vnd.github.raw+json",
            allow_not_found=True,
        )
        return result if isinstance(result, str) else ""

    def get_latest_release(self, full_name: str) -> dict[str, Any] | None:
        result = self.request(f"/repos/{full_name}/releases/latest", allow_not_found=True)
        return result if isinstance(result, dict) else None

    def upsert_issue(self, repository: str, title: str, body: str) -> tuple[str, str]:
        issues = self.request(f"/repos/{repository}/issues?state=open&per_page=100")
        if not isinstance(issues, list):
            raise GitHubError("Issue search response was not a list.")

        existing = next(
            (
                issue
                for issue in issues
                if issue.get("title") == title and "pull_request" not in issue
            ),
            None,
        )
        if existing:
            issue_number = existing["number"]
            updated = self.request(
                f"/repos/{repository}/issues/{issue_number}",
                method="PATCH",
                payload={"body": body},
            )
            return "updated", str(updated.get("html_url", ""))

        created = self.request(
            f"/repos/{repository}/issues",
            method="POST",
            payload={"title": title, "body": body},
        )
        return "created", str(created.get("html_url", ""))


@dataclasses.dataclass(frozen=True)
class RepoSnapshot:
    name: str
    full_name: str
    html_url: str
    description: str
    primary_language: str
    topics: tuple[str, ...]
    stars: int
    forks: int
    archived: bool
    fork: bool
    private: bool
    has_issues: bool
    pushed_at: dt.datetime
    license_name: str
    homepage: str
    readme: str = ""
    latest_release: str = ""

    @classmethod
    def from_api(
        cls,
        data: dict[str, Any],
        *,
        readme: str = "",
        latest_release: dict[str, Any] | None = None,
    ) -> "RepoSnapshot":
        pushed_raw = data.get("pushed_at") or data.get("updated_at")
        pushed_at = parse_github_datetime(pushed_raw)
        license_data = data.get("license") or {}
        return cls(
            name=str(data.get("name", "")),
            full_name=str(data.get("full_name", "")),
            html_url=str(data.get("html_url", "")),
            description=str(data.get("description") or ""),
            primary_language=str(data.get("language") or "Unspecified"),
            topics=tuple(data.get("topics") or []),
            stars=int(data.get("stargazers_count") or 0),
            forks=int(data.get("forks_count") or 0),
            archived=bool(data.get("archived")),
            fork=bool(data.get("fork")),
            private=bool(data.get("private")),
            has_issues=bool(data.get("has_issues", True)),
            pushed_at=pushed_at,
            license_name=str(license_data.get("spdx_id") or license_data.get("name") or ""),
            homepage=str(data.get("homepage") or ""),
            readme=readme,
            latest_release=str((latest_release or {}).get("tag_name") or ""),
        )


def parse_github_datetime(value: Any) -> dt.datetime:
    if not value:
        return dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)
    text = str(value).replace("Z", "+00:00")
    parsed = dt.datetime.fromisoformat(text)
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=dt.timezone.utc)


def load_config(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Config file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc
    required = ("owner", "profile_repository", "portfolio_message")
    missing = [key for key in required if not data.get(key)]
    if missing:
        raise SystemExit(f"Config is missing required keys: {', '.join(missing)}")
    return data


def days_since(moment: dt.datetime, now: dt.datetime) -> int:
    return max(0, (now - moment.astimezone(dt.timezone.utc)).days)


def repository_score(repo: RepoSnapshot, config: dict[str, Any], now: dt.datetime) -> int:
    priority = int(config.get("priority_repositories", {}).get(repo.name, 30))
    age = days_since(repo.pushed_at, now)
    if age <= 7:
        recency = 30
    elif age <= 30:
        recency = 22
    elif age <= 90:
        recency = 12
    elif age <= 180:
        recency = 6
    else:
        recency = 1

    completeness = 0
    completeness += 7 if repo.description else 0
    completeness += 5 if repo.readme.strip() else 0
    completeness += 3 if repo.topics else 0
    completeness += 2 if repo.license_name else 0
    completeness += 2 if repo.latest_release else 0
    social_proof = min(repo.stars, 10) + min(repo.forks, 5)
    penalty = 1000 if repo.archived or repo.private or repo.fork else 0
    return priority + recency + completeness + social_proof - penalty


def select_focus_repositories(
    repos: Iterable[RepoSnapshot],
    config: dict[str, Any],
    now: dt.datetime,
    limit: int = 3,
) -> list[RepoSnapshot]:
    excluded = set(config.get("excluded_repositories", []))
    eligible = [
        repo
        for repo in repos
        if repo.name not in excluded and not repo.archived and not repo.private and not repo.fork
    ]
    return sorted(
        eligible,
        key=lambda repo: (repository_score(repo, config, now), repo.pushed_at),
        reverse=True,
    )[:limit]


def strip_markdown(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^[#>*+\-\d.\s]+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[`*_~|]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def readme_summary(repo: RepoSnapshot, limit: int = 180) -> str:
    cleaned = strip_markdown(repo.readme)
    if cleaned.lower().startswith(repo.name.lower()):
        cleaned = cleaned[len(repo.name):].lstrip(" :-—")
    candidate = cleaned or repo.description or "Repository documentation is still being developed."
    return trim_to(candidate, limit)


def trim_to(text: str, limit: int) -> str:
    normalized = re.sub(r"\s+", " ", text).strip()
    if len(normalized) <= limit:
        return normalized
    if limit <= 1:
        return normalized[:limit]
    shortened = normalized[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:-")
    if not shortened:
        shortened = normalized[: limit - 1]
    return shortened + "…"


def repo_identity(repo: RepoSnapshot, config: dict[str, Any]) -> dict[str, str]:
    override = config.get("repo_overrides", {}).get(repo.name, {})
    return {
        "display_name": override.get("display_name", repo.name),
        "category": override.get("category", repo.primary_language + " project"),
        "positioning": override.get("positioning", repo.description or readme_summary(repo)),
        "audience": override.get("audience", "developers and potential users"),
    }


def proof_points(repo: RepoSnapshot, now: dt.datetime) -> list[str]:
    points: list[str] = []
    if repo.latest_release:
        points.append(f"Latest tagged release: {repo.latest_release}")
    points.append(f"Recent repository activity: {repo.pushed_at.date().isoformat()}")
    if repo.primary_language != "Unspecified":
        points.append(f"Primary language: {repo.primary_language}")
    if repo.topics:
        points.append("Topics: " + ", ".join(repo.topics[:5]))
    if repo.stars or repo.forks:
        points.append(f"GitHub signal: {repo.stars} star(s), {repo.forks} fork(s)")
    points.append("Repository-backed proof: README, source, and commit history")
    return points[:4]


def build_micro_post(repo: RepoSnapshot, config: dict[str, Any]) -> str:
    identity = repo_identity(repo, config)
    base = (
        f"Building {identity['display_name']}: {identity['positioning']} "
        f"The work is public, documented, and visible in the repo. {repo.html_url}"
    )
    return trim_to(base, 280)


def build_linkedin_post(repo: RepoSnapshot, config: dict[str, Any], now: dt.datetime) -> str:
    identity = repo_identity(repo, config)
    proof = proof_points(repo, now)
    return "\n".join(
        [
            f"This week’s project focus: {identity['display_name']}",
            "",
            identity["positioning"],
            "",
            "What I’m demonstrating through the repository:",
            *[f"• {item}" for item in proof],
            "",
            f"Built for {identity['audience']}. I’m sharing the actual project history rather than presenting it as more finished than it is.",
            "",
            repo.html_url,
        ]
    )


def build_devlog_post(repo: RepoSnapshot, config: dict[str, Any], now: dt.datetime) -> str:
    identity = repo_identity(repo, config)
    age = days_since(repo.pushed_at, now)
    if age == 0:
        activity = "today"
    elif age == 1:
        activity = "1 day ago"
    else:
        activity = f"{age} days ago"
    return "\n".join(
        [
            f"## {identity['display_name']} — repository spotlight",
            "",
            identity["positioning"],
            "",
            f"The repository was last pushed {activity}. The strongest proof is not a marketing claim; it is the combination of source, documentation, commit history, and the project’s visible constraints.",
            "",
            "### What to inspect",
            "",
            f"- Project overview: {readme_summary(repo)}",
            f"- Primary implementation language: {repo.primary_language}",
            f"- Best audience fit: {identity['audience']}",
            f"- Repository: {repo.html_url}",
            "",
            "### Suggested discussion question",
            "",
            f"What part of {identity['category'].lower()} development would be most useful to document next: architecture, validation, UI decisions, or release process?",
        ]
    )


def metadata_actions(repos: Iterable[RepoSnapshot]) -> list[str]:
    actions: list[str] = []
    for repo in repos:
        gaps: list[str] = []
        if not repo.description:
            gaps.append("add a concise GitHub description")
        if not repo.topics:
            gaps.append("add discoverability topics")
        if not repo.license_name:
            gaps.append("clarify licensing")
        if not repo.readme.strip():
            gaps.append("add a README")
        if gaps:
            actions.append(f"**{repo.name}:** " + "; ".join(gaps) + ".")
    return actions


def build_marketing_pack(
    repos: list[RepoSnapshot],
    config: dict[str, Any],
    now: dt.datetime,
) -> str:
    focus = select_focus_repositories(repos, config, now, limit=3)
    if not focus:
        raise ValueError("No eligible public repositories were found.")

    lines = [
        "# Keepithandy Weekly Repository Marketing Pack",
        "",
        f"**Generated:** {now.date().isoformat()}",
        "",
        f"**Portfolio narrative:** {config['portfolio_message']}",
        "",
        f"**Campaign goal:** {config.get('campaign_goal', 'Market current repository work honestly.')}",
        "",
        "## Recommended Focus",
        "",
    ]

    for index, repo in enumerate(focus, start=1):
        identity = repo_identity(repo, config)
        lines.extend(
            [
                f"### {index}. [{identity['display_name']}]({repo.html_url})",
                "",
                f"**Role:** {identity['category']}",
                "",
                f"**Positioning:** {identity['positioning']}",
                "",
                f"**Audience:** {identity['audience']}",
                "",
                "**Proof points:**",
                *[f"- {point}" for point in proof_points(repo, now)],
                "",
            ]
        )

    lead = focus[0]
    secondary = focus[1] if len(focus) > 1 else focus[0]
    tertiary = focus[2] if len(focus) > 2 else secondary

    lines.extend(
        [
            "## Ready-to-Review Copy",
            "",
            "### Short social post (280 characters maximum)",
            "",
            build_micro_post(lead, config),
            "",
            "### Professional network post",
            "",
            build_linkedin_post(secondary, config, now),
            "",
            "### GitHub Discussion / devlog post",
            "",
            build_devlog_post(tertiary, config, now),
            "",
            "## Suggested Weekly Sequence",
            "",
            f"- **Monday — Flagship proof:** Share {repo_identity(lead, config)['display_name']} with one concrete repository-backed proof point.",
            f"- **Wednesday — Technical depth:** Share {repo_identity(secondary, config)['display_name']} and explain one implementation or validation decision.",
            f"- **Friday — Conversation:** Post the {repo_identity(tertiary, config)['display_name']} devlog and ask the suggested discussion question.",
            "",
            "## Profile and Repository Hygiene",
            "",
        ]
    )

    actions = metadata_actions(repos)
    if actions:
        lines.extend([*[f"- {action}" for action in actions[:12]], ""])
    else:
        lines.extend(["- No obvious README, description, topic, or license gaps detected.", ""])

    lines.extend(
        [
            "## Guardrails",
            "",
            "- Review all copy before posting.",
            "- Do not claim unfinished prototypes are complete products.",
            "- Prefer repository proof over broad claims.",
            "- Do not auto-post, mass-message, or manufacture engagement.",
            "- Keep one primary call to action per post.",
            "",
            "---",
            "Generated by the draft-only Repo Marketing Agent in `keepithandy/keepithandy`.",
            "",
        ]
    )
    return "\n".join(lines)


def hydrate_repositories(
    client: GitHubClient,
    owner: str,
    raw_repositories: list[dict[str, Any]],
    excluded: set[str],
) -> list[RepoSnapshot]:
    snapshots: list[RepoSnapshot] = []
    for data in raw_repositories:
        name = str(data.get("name", ""))
        if name in excluded or data.get("archived") or data.get("private") or data.get("fork"):
            snapshots.append(RepoSnapshot.from_api(data))
            continue
        full_name = str(data.get("full_name", f"{owner}/{name}"))
        readme = client.get_readme(full_name)
        release = client.get_latest_release(full_name)
        snapshots.append(RepoSnapshot.from_api(data, readme=readme, latest_release=release))
    return snapshots


def load_fixture(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("Fixture must contain a JSON array of GitHub repository objects.")
    return data


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).with_name("config.json"),
        help="Path to marketing agent JSON configuration.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("marketing-pack.md"),
        help="Markdown output path.",
    )
    parser.add_argument(
        "--publish-issue",
        action="store_true",
        help="Create or update the rolling campaign issue in the profile repository.",
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        help="Use a local GitHub API fixture instead of requesting live repository data.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    config = load_config(args.config)
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    client = GitHubClient(token=token)
    owner = str(config["owner"])
    excluded = set(config.get("excluded_repositories", []))

    try:
        if args.fixture:
            raw_repositories = load_fixture(args.fixture)
            snapshots = [
                RepoSnapshot.from_api(
                    data,
                    readme=str(data.get("_readme") or ""),
                    latest_release=(
                        {"tag_name": data.get("_latest_release")}
                        if data.get("_latest_release")
                        else None
                    ),
                )
                for data in raw_repositories
            ]
        else:
            raw_repositories = client.list_owner_repositories(owner)
            snapshots = hydrate_repositories(client, owner, raw_repositories, excluded)
        timezone_name = str(config.get("timezone", "UTC"))
        try:
            timezone = ZoneInfo(timezone_name)
        except ZoneInfoNotFoundError as exc:
            raise ValueError(f"Unknown configured timezone: {timezone_name}") from exc
        now = dt.datetime.now(timezone)
        report = build_marketing_pack(snapshots, config, now)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote marketing pack: {args.output}")

        if args.publish_issue:
            if not token:
                raise SystemExit("--publish-issue requires GH_TOKEN or GITHUB_TOKEN.")
            action, url = client.upsert_issue(
                str(config["profile_repository"]),
                str(config.get("issue_title", "Repo Marketing Agent — Weekly Campaign Pack")),
                report,
            )
            print(f"{action.title()} rolling marketing issue: {url}")
    except (GitHubError, ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"marketing-agent error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
