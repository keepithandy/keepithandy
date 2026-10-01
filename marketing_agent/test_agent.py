import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agent import (  # noqa: E402
    RepoSnapshot,
    build_marketing_pack,
    build_micro_post,
    repository_score,
    select_focus_repositories,
    trim_to,
)

NOW = dt.datetime(2026, 7, 20, tzinfo=dt.timezone.utc)


def make_repo(name: str, days_old: int, description: str = "A useful project") -> RepoSnapshot:
    return RepoSnapshot(
        name=name,
        full_name=f"keepithandy/{name}",
        html_url=f"https://github.com/keepithandy/{name}",
        description=description,
        primary_language="Python",
        topics=("developer-tools",),
        stars=1,
        forks=0,
        archived=False,
        fork=False,
        private=False,
        has_issues=True,
        pushed_at=NOW - dt.timedelta(days=days_old),
        license_name="MIT",
        homepage="",
        readme=f"# {name}\n\n{description}",
        latest_release="v0.1.0",
    )


class MarketingAgentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = {
            "owner": "keepithandy",
            "profile_repository": "keepithandy/keepithandy",
            "portfolio_message": "Proof-based portfolio marketing.",
            "campaign_goal": "Generate honest drafts.",
            "excluded_repositories": [],
            "priority_repositories": {"DungeonDex": 100, "merge-guard": 80},
            "repo_overrides": {
                "DungeonDex": {
                    "display_name": "DungeonDex",
                    "category": "Flagship browser RPG",
                    "positioning": "A smoke-backed browser dungeon crawler.",
                    "audience": "players and developers",
                }
            },
        }

    def test_trim_to_respects_limit(self) -> None:
        result = trim_to("word " * 100, 40)
        self.assertLessEqual(len(result), 40)
        self.assertTrue(result.endswith("…"))

    def test_priority_and_recency_affect_score(self) -> None:
        flagship = make_repo("DungeonDex", 40)
        recent_tool = make_repo("merge-guard", 1)
        self.assertGreater(
            repository_score(flagship, self.config, NOW),
            repository_score(recent_tool, self.config, NOW),
        )

    def test_focus_selection_excludes_archived_repositories(self) -> None:
        active = make_repo("DungeonDex", 1)
        archived = dataclasses_replace(make_repo("old-project", 0), archived=True)
        focus = select_focus_repositories([archived, active], self.config, NOW)
        self.assertEqual([repo.name for repo in focus], ["DungeonDex"])

    def test_micro_post_stays_within_280_characters(self) -> None:
        repo = make_repo("DungeonDex", 1, "Detailed description " * 30)
        post = build_micro_post(repo, self.config)
        self.assertLessEqual(len(post), 280)
        self.assertIn("https://github.com/keepithandy/DungeonDex", post)

    def test_report_contains_required_review_sections(self) -> None:
        repos = [make_repo("DungeonDex", 1), make_repo("merge-guard", 2)]
        report = build_marketing_pack(repos, self.config, NOW)
        self.assertIn("## Ready-to-Review Copy", report)
        self.assertIn("## Suggested Weekly Sequence", report)
        self.assertIn("## Guardrails", report)


def dataclasses_replace(repo: RepoSnapshot, **changes: object) -> RepoSnapshot:
    values = repo.__dict__.copy()
    values.update(changes)
    return RepoSnapshot(**values)


if __name__ == "__main__":
    unittest.main()
