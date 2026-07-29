# Keepithandy Project Ecosystem Strategy

This document resolves the portfolio-wide discussion into a practical operating model.

## Portfolio shape

1. **Flagship games:** DungeonDex and The Apothecary Ledger demonstrate original loops, progression, UX, and release discipline.
2. **Reusable foundations:** Depth Engine and crafting-kit isolate reusable game architecture and data contracts.
3. **Developer and QA tools:** PatchLens, merge-guard, and dev-kit demonstrate testing, audit, reporting, and merge safety.
4. **Focused experiments:** DungeonDex3D, NovaDeck Analyst, Guildmasters, and other prototypes prove narrow ideas while remaining honestly labeled.
5. **Governance and safety:** Northline Studio Licensing and repair-tool-kit document ownership, provenance, and non-destructive workflows.

## Priority rules

- Keep DungeonDex stable and player-facing.
- Advance one secondary playable project at a time.
- Reuse proven contracts rather than duplicating systems.
- Require repository-backed proof before profile promotion.
- Prefer validation, mobile usability, and release hygiene over feature accumulation.
- Archive or demote projects whose purpose is no longer distinct.

## Connection opportunities

- PatchLens can consume release checklists from game repositories without writing to them automatically.
- merge-guard can recommend repository-specific checks discovered from package scripts and smoke files.
- dev-kit can audit version authority, documentation, and release readiness across public repositories.
- crafting-kit and Depth Engine can remain independent reference implementations until a real integration need is proven.
- Licensing and provenance templates should be adopted by each public project before broader distribution.

## Review cadence

Use the quarterly profile review and project-status template in `PROFILE_MAINTENANCE.md`. Portfolio promotion requires current status, a working entry point, validation evidence, limitations, and a next safe step.
