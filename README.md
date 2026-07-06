# Hi, I’m John / keepithandy

I build browser-based RPGs, reusable game-engine systems, read-only dashboards, and practical developer tools. My projects usually sit in the same lane: small playable systems, clean documentation, repeatable workflows, and tools that make future builds easier instead of messier.

Right now I’m building in public and using GitHub as a working portfolio: not just finished products, but proof that I can design systems, ship patches, document decisions, and keep projects moving.

## Main Projects

### [DungeonDex](https://github.com/keepithandy/DungeonDex)
A solo-developed browser dungeon crawler focused on compact mobile play, readable combat, gear progression, elite contracts, trophy records, dungeon memory, and a growing Talent system.

DungeonDex is my main systems-design project. It’s where I practice careful feature gates, smoke testing, save-safety, progression design, and long-term RPG architecture.

### [dev-kit](https://github.com/keepithandy/dev-kit)
A Python command-line toolkit for read-only project audits and release hygiene. It checks local repo folders for version-label drift, baseline files, smoke-script coverage, and Markdown report output.

This is part of my push to build useful non-JavaScript tooling around the projects I already maintain.

### [Depth Engine](https://github.com/keepithandy/depth-engine)
A lightweight browser RPG engine foundation built with plain HTML, CSS, and JavaScript. It separates reusable engine logic from example game content so future RPG themes can be copied, studied, and reshaped without starting from zero.

Current example: **Rat Cellar**, a simple proof-of-loop for combat, XP, loot, equipment, saves, export/import, and reset flows.

### [NovaDeck Analyst](https://github.com/keepithandy/crypto-analyst)
A mock-first, read-only crypto analysis dashboard starter focused on watchlists, market summaries, invalidation levels, scenario review, and LONG / SHORT / WATCH / FLAT trade-readiness labels.

NovaDeck Analyst is a research dashboard, not trade execution software.

## Secondary and Early-Stage Projects

- [guildmasters](https://github.com/keepithandy/guildmasters) — an early game/project concept for guild-style progression and management systems.
- [repair-tool-kit](https://github.com/keepithandy/repair-tool-kit) — a planned Windows maintenance and diagnostic toolkit.
- [crafting-kit](https://github.com/keepithandy/crafting-kit) — an early utility/project shell still being shaped.

## Current Roadmap

| Repo | Type | Status | Next useful issue |
| --- | --- | --- | --- |
| [DungeonDex](https://github.com/keepithandy/DungeonDex) | Browser RPG | Main active project | Board Echo v1 and Debt Pressure v1 clarity/recovery |
| [dev-kit](https://github.com/keepithandy/dev-kit) | Python developer tool | Active tooling repo | Portfolio audit mode across sibling repos |
| [Depth Engine](https://github.com/keepithandy/depth-engine) | Browser RPG engine foundation | Active reusable-engine prototype | Add a third bundled example to prove content authoring |
| [NovaDeck Analyst](https://github.com/keepithandy/crypto-analyst) | Read-only dashboard | Early v0.1 foundation | Mock dashboard shell and deterministic risk engine |
| [merge-guard](https://github.com/keepithandy/merge-guard) | PR safety CLI | Active developer tool | Suggest project-specific smoke/test commands |
| [guildmasters](https://github.com/keepithandy/guildmasters) | Idle guild-management game | Early playable loop | Add a compact Guild Log for contract history |
| [crafting-kit](https://github.com/keepithandy/crafting-kit) | Reusable crafting systems | Early validator/tooling repo | Add a read-only crafting dry-run simulator |
| [repair-tool-kit](https://github.com/keepithandy/repair-tool-kit) | Windows repair workflow docs/tooling | Planning-first safety repo | Add a safe maintenance checklist and notes template |
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
2. Growing dev-kit into a practical audit/reporting tool.
3. Strengthening Depth Engine into a reusable starter foundation.
4. Keeping NovaDeck Analyst scoped as a read-only dashboard project.
5. Keeping early projects organized enough that they can become real portfolio pieces instead of forgotten folders.

## How I Work

I like small, controlled changes with clear intent. A good patch should be easy to describe, easy to review, and safe to build on. That usually means read-only helpers first, smoke coverage before risky behavior, and documentation that explains what changed without pretending the project is bigger than it is.
