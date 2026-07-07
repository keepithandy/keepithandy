# Hi, I’m John / keepithandy

I build small browser RPGs, reusable game systems, read-only dashboards, and developer tools for safer project workflows.

Most of my work follows the same pattern: build a small system, document it clearly, protect it with smoke checks, then reuse what works.

Right now I’m building in public and using GitHub as a working portfolio: not just finished products, but proof that I can design systems, ship patches, document decisions, and keep projects moving.

## Best Places To Start

- [DungeonDex](https://github.com/keepithandy/DungeonDex) — my main browser RPG and systems-design project.
- [Depth Engine](https://github.com/keepithandy/depth-engine) — a reusable no-build browser RPG foundation.
- [merge-guard](https://github.com/keepithandy/merge-guard) — a pull request risk scanner for safer merges.
- [dev-kit](https://github.com/keepithandy/dev-kit) — a Python release-hygiene and repo-audit CLI.

## Quick Proof Points

| Project | What to look at first | Proof signal |
| --- | --- | --- |
| [DungeonDex](https://github.com/keepithandy/DungeonDex) | Current build notes, live systems list, and smoke target | Main RPG has playable loops, merchant gear upgrades, memory lanes, and compact smoke coverage. |
| [Depth Engine](https://github.com/keepithandy/depth-engine) | Bundled examples and smoke checks | Same engine core runs Rat Cellar, Arena Waves, and Sewer Patrol with no build step. |
| [merge-guard](https://github.com/keepithandy/merge-guard) | Example CLI output and risk report format | Produces merge-readiness reports from diffs, including risk flags and suggested checks. |
| [dev-kit](https://github.com/keepithandy/dev-kit) | PowerShell quick start and audit commands | Read-only Python CLI checks release hygiene across local project folders. |
| [NovaDeck Analyst](https://github.com/keepithandy/crypto-analyst) | Project safety model and decision labels | Read-only dashboard concept built around risk, invalidation, and LONG / SHORT / WATCH / FLAT labels. |

## Flagship and Active Projects

### [DungeonDex](https://github.com/keepithandy/DungeonDex)

A solo-developed browser dungeon crawler focused on compact mobile play, readable combat, gear progression, merchant upgrades, elite contracts, trophy records, dungeon memory, and safe smoke-backed patches.

DungeonDex is my main systems-design project. It’s where I practice careful feature gates, save-safety, progression design, player-facing system clarity, and long-term RPG architecture.

**Status:** Active flagship.

### [Depth Engine](https://github.com/keepithandy/depth-engine)

A lightweight browser RPG engine foundation built with plain HTML, CSS, and JavaScript. It separates reusable engine logic from example game content so future RPG themes can be copied, studied, and reshaped without starting from zero.

Current bundled examples include **Rat Cellar**, **Arena Waves**, and **Sewer Patrol** as proof that the same engine core can support different small RPG themes.

**Status:** Active reusable-engine prototype.

### [merge-guard](https://github.com/keepithandy/merge-guard)

A lightweight pull request and diff risk scanner for safer merges. It reads changes, flags risky files, explains likely breakage areas, and suggests review checks before a branch is merged.

This is my main developer-product experiment: a small tool aimed at making AI-assisted and solo-development workflows safer.

**Status:** Active developer-tool prototype.

### [dev-kit](https://github.com/keepithandy/dev-kit)

A Python command-line toolkit for read-only project audits and release hygiene. It checks local repo folders for version-label drift, baseline files, smoke-script coverage, and Markdown report output.

This is part of my push to build useful non-JavaScript tooling around the projects I already maintain.

**Status:** Active tooling repo.

### [NovaDeck Analyst](https://github.com/keepithandy/crypto-analyst)

A mock-first, read-only crypto analysis dashboard starter focused on watchlists, market summaries, invalidation levels, scenario review, and LONG / SHORT / WATCH / FLAT trade-readiness labels.

NovaDeck Analyst is a research dashboard, not trade execution software.

**Status:** Early v0.1 dashboard foundation.

## Supporting Projects and Experiments

- [guildmasters](https://github.com/keepithandy/guildmasters) — a small idle guild-management game with recruiting, contract resolution, guild upgrades, a readable Guild Log, and browser save/load.
- [crafting-kit](https://github.com/keepithandy/crafting-kit) — a reusable crafting-systems repo with starter content validation and read-only crafting dry-run helpers.
- [repair-tool-kit](https://github.com/keepithandy/repair-tool-kit) — a safety-first Windows repair workflow repo with manual maintenance checklists and repair-session notes.
- [DungeonDex3D](https://github.com/keepithandy/DungeonDex3D) — an experimental 3D dungeon prototype currently focused on archive adoption and a first graybox movement slice.

## Current Roadmap

| Repo | Type | Status | Next useful issue |
| --- | --- | --- | --- |
| [DungeonDex](https://github.com/keepithandy/DungeonDex) | Browser RPG | Active flagship | Board Echo v1, Debt Pressure v1, and public copy/smoke hardening |
| [Depth Engine](https://github.com/keepithandy/depth-engine) | Browser RPG engine foundation | Active reusable-engine prototype | Keep proving bundled examples and public starter-readiness |
| [merge-guard](https://github.com/keepithandy/merge-guard) | PR safety CLI | Active developer-tool prototype | Suggest project-specific smoke/test commands |
| [dev-kit](https://github.com/keepithandy/dev-kit) | Python developer tool | Active tooling repo | Portfolio audit mode across sibling repos |
| [NovaDeck Analyst](https://github.com/keepithandy/crypto-analyst) | Read-only dashboard | Early v0.1 foundation | Mock dashboard shell and deterministic risk engine |
| [guildmasters](https://github.com/keepithandy/guildmasters) | Idle guild-management game | Early playable loop | Continue compact progression/log polish |
| [crafting-kit](https://github.com/keepithandy/crafting-kit) | Reusable crafting systems | Early validator/tooling repo | Expand dry-run helpers toward more recipe cases |
| [repair-tool-kit](https://github.com/keepithandy/repair-tool-kit) | Windows repair workflow docs/tooling | Planning-first safety repo | Add a read-only system information collector |
| [DungeonDex3D](https://github.com/keepithandy/DungeonDex3D) | Experimental 3D dungeon prototype | Archive-adoption phase | Extract source archive, define run commands, then build a graybox slice |

## What I’m Building Toward

I’m interested in the overlap between game design, systems thinking, AI-assisted development, and developer productivity. The long-term goal is to build a reusable foundation for browser-based RPGs while also creating practical tools that help with real development work.

The common thread across my repos is simple: build the system, explain the system, test the system, then reuse what works.

## Tech and Tools

I work across:

- JavaScript and TypeScript for interactive browser projects
- HTML and CSS for lightweight, no-build-step prototypes
- React and Vite for dashboard-style apps
- Python for automation, audits, and developer tooling
- Markdown for project notes, documentation, and release summaries
- Git and GitHub for version control, issue tracking, and public project history

## Current Focus

Right now I’m focused on:

1. Continuing DungeonDex as the main RPG systems project.
2. Strengthening Depth Engine into a reusable starter foundation.
3. Growing merge-guard and dev-kit into practical developer workflow tools.
4. Keeping NovaDeck Analyst scoped as a read-only dashboard project.
5. Keeping experiments honest about their status so they can become real portfolio pieces instead of forgotten folders.

## How I Work

I like small, controlled changes with clear intent. A good patch should be easy to describe, easy to review, and safe to build on. That usually means read-only helpers first, smoke coverage before risky behavior, and documentation that explains what changed without pretending the project is bigger than it is.
