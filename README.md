# Hi, I’m John / keepithandy

I build browser games, reusable game systems, read-only dashboards, mobile-first QA tools, and developer utilities for safer project workflows.

Most of my work follows the same pattern: build a small system, document it clearly, protect it with focused smoke checks, then reuse what works.

Right now I’m building in public and using GitHub as a working portfolio: not just finished products, but proof that I can design systems, ship controlled patches, document decisions, validate releases, and keep projects moving.

## Best Places To Start

- [DungeonDex](https://github.com/keepithandy/DungeonDex) — flagship browser RPG and longest-running systems project.
- [The Apothecary Ledger](https://github.com/keepithandy/alchemy-game) — self-contained browser alchemy game with process-sensitive brewing and shop progression.
- [PatchLens](https://github.com/keepithandy/patch-lens) — mobile-first QA workspace for test sessions, defects, regressions, and developer-ready reports.
- [Depth Engine](https://github.com/keepithandy/depth-engine) — reusable no-build browser RPG foundation.
- [merge-guard](https://github.com/keepithandy/merge-guard) — pull request risk scanner for safer merges.
- [dev-kit](https://github.com/keepithandy/dev-kit) — Python release-hygiene and repository-audit CLI.

## Current-State Proof

These are compact, repository-backed proof points rather than mock marketing screenshots.

<details>
<summary><strong>DungeonDex — versioned, smoke-backed browser RPG</strong></summary>

- Current version authority: **v1.26.4.04 — Boss Curve Release**.
- The repository maintains explicit version authority, changelog history, release notes, build/cache labels, and focused smoke contracts.
- Current maintenance direction emphasizes mobile readability, CSS/QoL, release hygiene, and preservation of the established gameplay loop.

**Start here:** [VERSION.md](https://github.com/keepithandy/DungeonDex/blob/main/VERSION.md) · [README](https://github.com/keepithandy/DungeonDex#readme) · [commit history](https://github.com/keepithandy/DungeonDex/commits/main)

</details>

<details>
<summary><strong>The Apothecary Ledger — complete browser alchemy prototype loop</strong></summary>

```text
Forage for ingredients
→ inspect hidden traits
→ configure the brewing process
→ discover formulas
→ fulfill orders or sell stock
→ improve the workshop
→ repeat
```

- Current baseline: **v0.1.0 prototype**.
- Plain HTML, CSS, and JavaScript with no package manager, build step, account, API key, or server requirement.
- The prototype includes 12 ingredients, 15 possible effects, two- and three-ingredient mixtures, process-sensitive brewing, hidden-effect discovery, customer orders, potion storage, workshop upgrades, local saves, mobile layouts, and built-in browser smoke checks.

**Start here:** [README and gameplay loop](https://github.com/keepithandy/alchemy-game#readme) · [source](https://github.com/keepithandy/alchemy-game/tree/main) · [commit history](https://github.com/keepithandy/alchemy-game/commits/main)

</details>

<details>
<summary><strong>PatchLens — local-first QA workflow for browser projects</strong></summary>

```text
Select project
→ start versioned test session
→ run release checklist
→ capture evidence-backed defects
→ track regression status
→ export Markdown or Codex-ready report
```

- Current baseline: **v0.1.0 — Prototype Baseline**.
- Mobile-first dashboard with project tracking, device/browser metadata, pass/fail/N/A checklists, structured defect capture, severity and regression states, Markdown reports, constrained repair prompts, JSON backup, and LocalStorage persistence.
- Dependency-free PWA architecture with an offline shell, service worker, manifest, focused smoke harness, and no backend, account system, telemetry, or automatic GitHub writes.

**Start here:** [README and workflow](https://github.com/keepithandy/patch-lens#readme) · [application shell](https://github.com/keepithandy/patch-lens/blob/main/index.html) · [smoke test](https://github.com/keepithandy/patch-lens/blob/main/smoke_model.mjs)

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

The CLI supports text, Markdown, JSON, CI thresholds, per-file scoring, custom rules, PR context, repository-aware suggested checks, PR comments, npm/npx packaging, and a reusable GitHub Action.

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
- The repository proves the watchlist, asset-detail, deterministic risk-label, invalidation, and explanation foundations.
- A portfolio screenshot remains deferred until the v0.1 visual shell is stable enough to represent the project honestly.

**Start here:** [README and safety boundary](https://github.com/keepithandy/crypto-analyst#readme) · [source](https://github.com/keepithandy/crypto-analyst/tree/main/src)

</details>

## Flagship and Active Projects

### [DungeonDex](https://github.com/keepithandy/DungeonDex)

A solo-developed browser dungeon crawler focused on compact mobile play, readable combat, gear progression, merchant upgrades, elite contracts, trophy records, dungeon memory, and safe smoke-backed patches.

**Status:** Active flagship. Current work is intentionally biased toward controlled gameplay tuning, QoL, CSS, mobile clarity, IP presentation, and release safety.

### [The Apothecary Ledger](https://github.com/keepithandy/alchemy-game)

A self-contained browser alchemy game built around hidden ingredient properties, process-sensitive potion brewing, customer orders, discovery, and workshop progression.

**Status:** Playable v0.1.0 prototype with a complete local gameplay loop, automatic browser saves, mobile support, and built-in smoke validation.

### [PatchLens](https://github.com/keepithandy/patch-lens)

A mobile-first quality-assurance companion that converts informal browser and game testing into versioned test sessions, reproducible defect records, regression states, release reports, and constrained repair prompts.

**Status:** Functional v0.1.0 local-first PWA baseline published on `main`.

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

The strongest current six-repository portfolio set is:

1. [DungeonDex](https://github.com/keepithandy/DungeonDex) — flagship product and deepest systems history.
2. [alchemy-game](https://github.com/keepithandy/alchemy-game) — complete original gameplay loop and polished no-build browser delivery.
3. [patch-lens](https://github.com/keepithandy/patch-lens) — practical mobile-first QA workflow built from a recurring real development need.
4. [depth-engine](https://github.com/keepithandy/depth-engine) — reusable engine architecture and multi-example proof.
5. [merge-guard](https://github.com/keepithandy/merge-guard) — developer tool with concrete CLI/CI output.
6. [dev-kit](https://github.com/keepithandy/dev-kit) — Python automation and release-audit work.

Applying this order is a manual GitHub profile-setting step; this README records the reviewed order without claiming the profile pins were changed automatically.

## Current Roadmap

- **DungeonDex:** preserve the established loop while continuing narrow gameplay tuning, mobile, CSS, QoL, lore-presentation, and release-hygiene work.
- **The Apothecary Ledger:** validate balance, brewing clarity, mobile usability, and save reliability before expanding the ingredient or order catalog.
- **PatchLens:** use the v0.1.0 baseline on real project tests, then add editable checklist templates, defect deduplication, regression linking, and screenshot annotation.
- **Depth Engine:** complete the final unrestricted-browser gate for the v0.7 starter candidate before release labeling.
- **merge-guard:** harden release/versioning and expand real-repository validation without weakening diff authority.
- **dev-kit:** continue safe, read-only repository and release audits.
- **NovaDeck Analyst:** finish a stable mock-first v0.1 visual shell before adding screenshot proof or live data.
- **DungeonDex3D:** keep alpha work narrow around readability, controls, runtime reliability, and smoke coverage.

## What I’m Building Toward

I’m interested in the overlap between game design, systems thinking, AI-assisted development, and developer productivity. The long-term goal is to build a connected portfolio of original browser games, reusable foundations, and practical tools that make testing and releasing software safer.

The common thread across my repositories is simple: build the system, explain the system, test the system, then reuse what works.

## Tech and Tools

- JavaScript and TypeScript for interactive browser projects
- HTML and CSS for lightweight, no-build-step prototypes
- React, Vite, Three.js, and React Three Fiber for app and 3D experiments
- Python for automation, audits, and developer tooling
- LocalStorage, JSON portability, manifests, and service workers for local-first PWAs
- Focused smoke tests for release confidence and regression protection
- Markdown for project notes, documentation, QA reports, and release summaries
- Git and GitHub for version control, issue tracking, review, and public project history

## How I Work

I prefer small, controlled changes with clear intent. A good patch should be easy to describe, easy to review, and safe to build on. That usually means read-only helpers first, smoke coverage before risky behavior, explicit version authority, and documentation that explains what changed without pretending the project is bigger than it is.
