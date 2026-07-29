# Hi, I’m John / keepithandy

I build browser games, reusable game systems, local-first QA tools, read-only dashboards, and developer utilities. My working pattern is consistent: build a narrow system, document it, protect it with focused checks, and reuse only what proves useful.

## Best Places To Start

- [DungeonDex](https://github.com/keepithandy/DungeonDex) — flagship browser RPG and longest-running systems project.
- [The Apothecary Ledger](https://github.com/keepithandy/alchemy-game) — self-contained browser alchemy game with a complete local loop.
- [PatchLens](https://github.com/keepithandy/patch-lens) — mobile-first QA workspace for test sessions, defects, regressions, and reports.
- [Depth Engine](https://github.com/keepithandy/depth-engine) — reusable no-build browser RPG foundation.
- [merge-guard](https://github.com/keepithandy/merge-guard) — pull-request risk scanner.
- [dev-kit](https://github.com/keepithandy/dev-kit) — read-only Python repository and release audit CLI.

## Repository-Backed Proof

<details>
<summary><strong>DungeonDex — versioned, smoke-backed browser RPG</strong></summary>

- Current authority and release details are maintained in [VERSION.md](https://github.com/keepithandy/DungeonDex/blob/main/VERSION.md), the [README](https://github.com/keepithandy/DungeonDex#readme), and the [main history](https://github.com/keepithandy/DungeonDex/commits/main).
- Current maintenance favors controlled tuning, mobile readability, CSS/QoL, IP presentation, and release safety.
- This profile does not claim production readiness; repository version and validation files remain authoritative.

</details>

<details>
<summary><strong>Depth Engine — reusable core and bundled examples</strong></summary>

```text
Open index.html directly
→ choose a bundled example
→ play through the shared engine shell
→ validate save and content contracts
```

- No package manager or build step is required for the browser runtime.
- The v0.7 starter candidate remains candidate-labeled until its unrestricted-browser persistence/import/export gate is completed.
- Evidence: [README](https://github.com/keepithandy/depth-engine#readme), [examples](https://github.com/keepithandy/depth-engine/tree/main/examples), and [smoke workflow](https://github.com/keepithandy/depth-engine/blob/main/.github/workflows/smoke.yml).

</details>

<details>
<summary><strong>merge-guard — diff risk report</strong></summary>

```text
Risk level: MEDIUM
Merge readiness: NEEDS_REVIEW
Per-file risk: state/config changes detected
Suggested checks: tests, focused smoke, manual save review
```

The CLI supports text, Markdown, JSON, CI thresholds, per-file scoring, custom rules, PR context, repository-aware checks, npm/npx use, and a reusable Action. Evidence: [README](https://github.com/keepithandy/merge-guard#readme), [sample diff](https://github.com/keepithandy/merge-guard/blob/main/examples/sample.diff), and [Action](https://github.com/keepithandy/merge-guard/blob/main/action.yml).

</details>

<details>
<summary><strong>DungeonDex3D — v0.0.1-alpha graybox</strong></summary>

- Standalone React, Vite, TypeScript, Three.js, and React Three Fiber alpha.
- Current proof covers first-person movement, arena boundaries, pointer-lock recovery, encounter HUD, queued notifications, responsive layouts, resource fallbacks, typecheck, build, and smoke CI.
- The project remains an experimental alpha, not a production release.
- Evidence: [README and commands](https://github.com/keepithandy/DungeonDex3D#readme), [Alpha Quality workflow](https://github.com/keepithandy/DungeonDex3D/blob/main/.github/workflows/alpha-quality.yml), and [alpha smoke](https://github.com/keepithandy/DungeonDex3D/blob/main/scripts/smoke-alpha-hardening.mjs).

</details>

<details>
<summary><strong>dev-kit — read-only audit proof</strong></summary>

```text
python -m dev_kit audit --path <project> --profile dungeondex
PASS / WARN / FAIL summary
Recommended action: correct version or baseline drift before release
```

The example format is documented in the stable [sample report](https://github.com/keepithandy/dev-kit/blob/main/docs/SAMPLE_REPORT.md). The tool reads target repositories and writes only an explicitly requested report path. Evidence: [README](https://github.com/keepithandy/dev-kit#readme), [tests](https://github.com/keepithandy/dev-kit/tree/main/tests), and [report documentation](https://github.com/keepithandy/dev-kit#report-output).

</details>

<details>
<summary><strong>Guildmasters — playable idle loop</strong></summary>

```text
Recruit hero
→ assign contract with visible success chance
→ resolve success or failure
→ collect rewards and experience
→ upgrade guild
→ review Guild Log
```

The browser game includes recruitable heroes, contracts, rewards, upgrades, unlock copy, a Guild Log, and browser save/load. Current target: v0.2 progression spine and Guild Log polish; feature creep remains intentionally limited. Evidence: [README](https://github.com/keepithandy/guildmasters#readme), [source entry](https://github.com/keepithandy/guildmasters/blob/main/index.html), and the documented `npm run smoke` command.

</details>

<details>
<summary><strong>Northline Studio Licensing — scope and authority</strong></summary>

- Source code follows the controlling project or file license.
- Creative content follows project/asset terms and is otherwise reserved.
- Third-party material follows its original terms.
- Project-specific, file-specific, and third-party terms control conflicts; the hub is documentation, not legal certification or government registration.
- Evidence: [policy hub](https://github.com/keepithandy/Northline-Studio-Licensing#readme), [project catalog](https://github.com/keepithandy/Northline-Studio-Licensing/blob/main/PROJECTS.md), and [creative-content terms](https://github.com/keepithandy/Northline-Studio-Licensing/blob/main/ASSETS_LICENSE.md).

</details>

NovaDeck Analyst remains mock-first and read-only; screenshot proof is deferred until the visual shell is representative. No wallet, exchange-account, private-key, or trade-execution claim is made. See its [README](https://github.com/keepithandy/crypto-analyst#readme).

## Project Visibility

- **Flagship:** DungeonDex.
- **Active playable:** The Apothecary Ledger and PatchLens baseline.
- **Supporting foundations/tools:** Depth Engine, merge-guard, dev-kit, crafting-kit, and repair-tool-kit.
- **Experimental:** DungeonDex3D, NovaDeck Analyst, Guildmasters, Catalyst, and other explicitly early prototypes.
- **Private sandbox:** GitHub Practice App; private details are not used as public proof.
- **Archived:** shown only when historical context is useful and clearly labeled.

Full promotion, removal, mobile, and freshness rules are in [Profile Maintenance](docs/PROFILE_MAINTENANCE.md). The portfolio operating model is in [Ecosystem Strategy](docs/ECOSYSTEM_STRATEGY.md).

## Recommended Pinned Order

1. [DungeonDex](https://github.com/keepithandy/DungeonDex)
2. [alchemy-game](https://github.com/keepithandy/alchemy-game)
3. [patch-lens](https://github.com/keepithandy/patch-lens)
4. [depth-engine](https://github.com/keepithandy/depth-engine)
5. [merge-guard](https://github.com/keepithandy/merge-guard)
6. [dev-kit](https://github.com/keepithandy/dev-kit)

This is the reviewed order. Applying profile pins remains a manual GitHub UI action; this README does not claim the UI setting was changed automatically.

## Maintenance and Validation

```powershell
python tools/check_profile.py
```

The profile workflow checks public README links and reports advisory wording that may overstate stability, completeness, security, scale, or validation. Temporary/deferred exceptions require an exact URL and reason in `profile-link-suppressions.json`; private targets are not exposed.

Quarterly reviews use [Profile Maintenance](docs/PROFILE_MAINTENANCE.md) to verify current status, version authority, validation evidence, limitations, and next safe work.

## Current Direction

- Preserve DungeonDex while continuing narrow player-facing polish and release hygiene.
- Complete Depth Engine's unrestricted-browser release gate before changing its candidate label.
- Use PatchLens on real test sessions and strengthen its reporting workflow.
- Harden merge-guard and dev-kit through real-repository fixtures and stable output contracts.
- Keep NovaDeck Analyst read-only and mock-first until its v0.1 shell is stable.
- Keep DungeonDex3D alpha work focused on controls, readability, runtime reliability, and playtesting rather than system expansion.

## Tech and Working Style

JavaScript, TypeScript, HTML, CSS, React, Vite, Three.js, React Three Fiber, Python, LocalStorage, JSON, PWAs, focused smoke tests, Markdown documentation, Git, and GitHub.

I prefer small controlled changes with explicit intent, evidence, limitations, and a safe next step.