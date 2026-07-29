#!/usr/bin/env python3
"""Validate profile links and advisory claim language without rewriting content."""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SUPPRESSIONS = ROOT / "profile-link-suppressions.json"
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\((https?://[^)]+)\)")
RISKY = re.compile(r"\b(production[- ]ready|fully tested|complete|secure|enterprise)\b", re.I)
ALLOW_CONTEXT = re.compile(r"\b(prototype|alpha|candidate|mock-first|manual gate|not production|evidence|validated|baseline)\b", re.I)


def load_suppressions() -> dict[str, str]:
    if not SUPPRESSIONS.exists():
        return {}
    data = json.loads(SUPPRESSIONS.read_text(encoding="utf-8"))
    return {item["url"]: item["reason"] for item in data.get("suppressions", []) if item.get("url") and item.get("reason")}


def check_url(url: str) -> str | None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "keepithandy-profile-check/1"})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if 200 <= response.status < 400:
                    return None
                return f"HTTP {response.status}"
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 405, 429):
                return None  # reachable or rate/method limited; not a missing public target
            return f"HTTP {exc.code}"
        except urllib.error.URLError as exc:
            if attempt == 0:
                time.sleep(1)
                continue
            return f"network error: {exc.reason}"
    return "unreachable"


def main() -> int:
    lines = README.read_text(encoding="utf-8").splitlines()
    suppressions = load_suppressions()
    failures: list[str] = []
    warnings: list[str] = []

    seen: set[str] = set()
    for number, line in enumerate(lines, 1):
        for label, url in LINK_RE.findall(line):
            if url in seen:
                continue
            seen.add(url)
            if url in suppressions:
                print(f"SUPPRESSED line {number}: {label} — {suppressions[url]}")
                continue
            problem = check_url(url)
            if problem:
                failures.append(f"README.md:{number}: {label!r} -> {url}: {problem}")

        if RISKY.search(line) and not ALLOW_CONTEXT.search(" ".join(lines[max(0, number-2):min(len(lines), number+1)])):
            warnings.append(f"README.md:{number}: unsupported production-style wording: {line.strip()}")

    if warnings:
        print("Advisory wording warnings:")
        print("\n".join(warnings))
        print("Suggested neutral terms: prototype, alpha, candidate, validated baseline, or link nearby evidence.")

    if failures:
        print("Profile link failures:")
        print("\n".join(failures))
        return 1

    print(f"Profile validation passed: {len(seen)} unique public links checked; {len(warnings)} advisory wording warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
