# Hi, I’m John / keepithandy

I build small browser RPGs, reusable game systems, read-only dashboards, and developer tools for safer project workflows.

Most of my work follows the same pattern: build a small system, document it clearly, protect it with smoke checks, then reuse what works.

Right now I’m building in public and using GitHub as a working portfolio: not just finished products, but proof that I can design systems, ship controlled patches, document decisions, and keep projects moving.

## Best Places To Start

- [DungeonDex](https://github.com/keepithandy/DungeonDex) — flagship browser RPG and systems-design project.
- [Depth Engine](https://github.com/keepithandy/depth-engine) — reusable no-build browser RPG foundation.
- [merge-guard](https://github.com/keepithandy/merge-guard) — pull request risk scanner for safer merges.
- [dev-kit](https://github.com/keepithandy/dev-kit) — Python release-hygiene and repository-audit CLI.

## Current-State Proof

These are compact, repository-backed proof points rather than mock marketing screenshots.

<details>
<summary><strong>DungeonDex — versioned, smoke-backed browser RPG</strong></summary>

- Current version authority: **v1.26.3.02 — Town Runtime Layer Cleanup**.
- The repository maintains explicit version authority, changelog history, release notes, and focused smoke contracts.
- Current maintenance direction emphasizes mobile readability, CSS/QoL, release hygiene, and preservation of the established gameplay loop.

**Start here:** [VERSION.md](https://github.com/keepithandy/DungeonDex/blob/main/VERSION.md) · [README](https://github.com/keepithandy/DungeonDex#readme) · [commit history](https://github.com/keepithandy/DungeonDex/commits/main)

</details>

<details>
<summary><strong>Depth Engine — four examples on one reusable core</strong></summary>

```text
Open index.html directly
→ Rat Cellar
→ Arena Waves
→ Sewer Patrol
→ Depth Kit Lab
```

- No install, package manager, build step, or local server is required for the browser runtime.
- Nine documented smoke commands cover the shell, example selection, engine core, save behavior, and bundled content.
- The current v0.7 starter candidate remains prototype-labeled until its final unrestricted-browser persistence/import/export gate is completed.

**Start here:** [README and smoke commands](https://github.com/keepithandy/depth-engine#readme) · [examples](https://github.com/keepithandy/depth-engine/tree/main/examples) · [smoke workflow](https://github.com/keepithandy/depth-engine/blob/main/.github/workflows/smoke.yml)

</details>

<details>
<summary><strong>merge-guard — real report output from a diff</strong></summary>

```text
merge-guard report
Risk level: MEDIUM
Merge readiness: NEEDS_REVIEW
Risk score: 4

Per-file risk:
- MEDIUM src/saveState.js — state or persistence logic changed
- MEDIUM package.json — dependency or config changed

Suggested checks:
- Run the normal test suite
- Run smoke tests related to changed systems
- Manually review save/load behavior
```

The CLI now supports text, Markdown, JSON, CI thresholds, per-file scoring, custom rules, PR context, repository-aware suggested checks, PR comments, npm/npx packaging, and a reusable GitHub Action.

**Start here:** [README and demo](https://github.com/keepithandy/merge-guard#readme) · [sample diff](https://github.com/keepithandy/merge-guard/blob/main/examples/sample.diff) · [Action definition](https://github.com/keepithandy/merge-guard/blob/main/action.yml)

</details>

<details>
<summary><strong>NovaDeck Analyst — read-only risk dashboard foundation</strong></summary>

```text
BTC / ETH / SOL / XRP
→ market structure
→ invalidation level
→ scenario weighting
→ LONG / SHORT / WATCH / FLAT
```

- Mock-data-first and read-only.
- No trade execution, wallet connection, private keys, exchange accounts, or prediction claims.
- The repository currently proves the watchlist, asset-detail, deterministic risk-label, invalidation, and explanation foundations.
- A portfolio screenshot is intentionally deferred until the v0.1 visual shell is stable enough to represent the project honestly.

**Start here:** [README and safety boundary](https://github.com/keepithandy/crypto-analyst#readme) · [source](https://github.com/keepithandy/crypto-analyst/tree/main/src)

</details>

## Flagship and Active Projects

### [DungeonDex](https://github.com/keepithandy/DungeonDex)

A solo-developed browser dungeon crawler focused on compact mobile play, readable combat, gear progression, merchant upgrades, elite contracts, trophy records, dungeon memory, and safe smoke-backed patches.

**Status:** Active flagship. Current work is intentionally biased toward QoL, CSS, mobile clarity, IP presentation, and release safety rather than new gameplay systems.

### [Depth Engine](https://github.com/keepithandy/depth-engine)

A lightweight browser RPG engine foundation built with plain HTML, CSS, and JavaScript. It separates reusable engine logic from example content so new themes can be copied, studied, and reshaped without starting from zero.

**Status:** Active reusable-engine prototype with a v0.7 starter candidate pending its final manual browser gate.

### [merge-guard](https://github.com/keepithandy/merge-guard)

A lightweight pull request and diff risk scanner that explains risky files, likely breakage areas, and relevant checks before a branch is merged.

**Status:** Active developer-tool prototype with CLI, CI, Action, custom-rule, PR-context, and project-check foundations implemented.

### [dev-kit](https://github.com/keepithandy/dev-kit)

A Python command-line toolkit for read-only project audits and release hygiene. It checks local repository folders for version-label drift, baseline files, smoke-script coverage, and Markdown report output.

**Status:** Active tooling repository.

### [NovaDeck Analyst](https://github.com/keepithandy/crypto-analyst)

A mock-first, read-only crypto analysis dashboard focused on watchlists, market summaries, invalidation levels, scenario review, and LONG / SHORT / WATCH / FLAT trade-readiness labels.

**Status:** Early v0.1 dashboard foundation; not trade-execution software.

## Supporting Projects and Experiments

- [guildmasters](https://github.com/keepithandy/guildmasters) — small idle guild-management game with recruiting, contracts, upgrades, a Guild Log, and browser save/load.
- [crafting-kit](https://github.com/keepithandy/crafting-kit) — reusable crafting-system validation and read-only crafting dry-run helpers.
- [repair-tool-kit](https://github.com/keepithandy/repair-tool-kit) — safety-first Windows repair workflows, maintenance checklists, and repair-session notes.
- [DungeonDex3D](https://github.com/keepithandy/DungeonDex3D) — `v0.0.1-alpha` playable graybox with a standalone React/Three.js build, first-person movement, encounter HUD, and focused runtime checks.
- [Northline Studio Licensing](https://github.com/keepithandy/Northline-Studio-Licensing) — licensing and studio-policy repository.
- [GitHub Practice App](https://github.com/keepithandy/Github-Practice-App) — small repository used for GitHub workflow practice.

## Recommended Pinned Repository Order

The reviewed six-repository portfolio set is:

1. [DungeonDex](https://github.com/keepithandy/DungeonDex) — flagship product and deepest systems history.
2. [depth-engine](https://github.com/keepithandy/depth-engine) — reusable engine architecture and multi-example proof.
3. [merge-guard](https://github.com/keepithandy/merge-guard) — developer tool with concrete CLI/CI output.
4. [dev-kit](https://github.com/keepithandy/dev-kit) — non-JavaScript automation and release-audit work.
5. [crypto-analyst](https://github.com/keepithandy/crypto-analyst) — React/Vite dashboard and explicit safety model.
6. [guildmasters](https://github.com/keepithandy/guildmasters) — compact playable game loop.

Applying this order is a manual GitHub profile-setting step; the repository README records the reviewed order without claiming the profile pins were changed automatically.

## Current Roadmap

- **DungeonDex:** preserve the established loop while continuing narrow mobile, CSS, QoL, lore-presentation, and release-hygiene work.
- **Depth Engine:** complete the final unrestricted-browser gate for the v0.7 starter candidate before release labeling.
- **merge-guard:** harden release/versioning and expand real-repository validation without weakening diff authority.
- **dev-kit:** continue safe, read-only repository and release audits.
- **NovaDeck Analyst:** finish a stable mock-first v0.1 visual shell before adding screenshot proof or live data.
- **DungeonDex3D:** keep alpha work narrow around readability, controls, runtime reliability, and smoke coverage.

## What I’m Building Toward

I’m interested in the overlap between game design, systems thinking, AI-assisted development, and developer productivity. The long-term goal is to build reusable foundations for browser RPGs while also creating practical tools that help with real development work.

The common thread across my repositories is simple: build the system, explain the system, test the system, then reuse what works.

## Tech and Tools

- JavaScript and TypeScript for interactive browser projects
- HTML and CSS for lightweight, no-build-step prototypes
- React, Vite, Three.js, and React Three Fiber for app and 3D experiments
- Python for automation, audits, and developer tooling
- Markdown for project notes, documentation, and release summaries
- Git and GitHub for version control, issue tracking, review, and public project history

## How I Work

I prefer small, controlled changes with clear intent. A good patch should be easy to describe, easy to review, and safe to build on. That usually means read-only helpers first, smoke coverage before risky behavior, and documentation that explains what changed without pretending the project is bigger than it is.
