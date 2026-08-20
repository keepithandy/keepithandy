# Repo Marketing Agent

A draft-only GitHub marketing workflow for the repositories owned by `keepithandy`.

The agent reads public repository metadata, README content, release tags, activity dates, topics, language, stars, forks, and basic documentation hygiene. It then produces a weekly campaign pack built around repository-backed proof.

## What it does

- ranks eligible repositories using configurable portfolio priority, recency, documentation completeness, and modest GitHub activity signals;
- selects three weekly focus repositories;
- writes a short social post, a professional-network post, and a GitHub Discussion/devlog draft;
- proposes a Monday/Wednesday/Friday campaign sequence;
- flags missing descriptions, topics, licenses, or READMEs;
- creates or updates one rolling issue in `keepithandy/keepithandy` when run by GitHub Actions.

## What it does not do

- It does not auto-post to X, LinkedIn, Reddit, TikTok, Discord, or other platforms.
- It does not send direct messages or manufacture engagement.
- It does not describe prototypes as finished products.
- It does not require a paid AI API or third-party dependency.

## Run locally

From the repository root:

```powershell
python marketing_agent/agent.py --output marketing-pack.md
```

Run validation:

```powershell
python -m unittest discover -s marketing_agent -p "test_*.py"
```

A GitHub token is optional for public metadata. It is required only when using `--publish-issue`:

```powershell
$env:GH_TOKEN = "YOUR_TOKEN"
python marketing_agent/agent.py --output marketing-pack.md --publish-issue
```

Do not commit personal access tokens.

## Configuration

Edit `marketing_agent/config.json` to change:

- portfolio narrative;
- campaign goal;
- excluded repositories;
- repository priority weights;
- project display names, positioning, audience, and category.

The repository overrides are intentionally factual and conservative. They give the deterministic agent enough context to produce usable copy without inventing project claims.

## GitHub Actions behavior

`.github/workflows/repo-marketing-agent.yml` runs every Monday and can also be triggered manually. It:

1. checks out the profile repository;
2. sets up Python;
3. runs the unit tests;
4. generates `marketing-pack.md`;
5. writes the report to the workflow summary;
6. creates or updates the rolling marketing issue.

The workflow requests only `contents: read` and `issues: write` permissions.

## Safe publishing workflow

Treat the generated issue as a review queue:

1. verify that each project claim still matches the repository;
2. choose one post rather than publishing every draft;
3. add a current screenshot, clip, changelog excerpt, or concrete code proof;
4. publish manually on the platform that fits the audience;
5. record useful audience feedback as a GitHub issue only when it affects the project roadmap.
