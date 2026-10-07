# John / keepithandy

<p align="center">
  <strong>Scratch-trained coding models · browser games · simulations · developer tools</strong><br>
  Building small, focused systems from the model weights up to the player-facing interface.
</p>

---

## Best Places to Start

- **[Plex Nano](https://github.com/Keepithandy/plex-nano-27m-v0.0.1-p2-24)** — my scratch-trained, repository-native coding-model research project.
- **[DungeonDex](https://northline-studio.itch.io/dungeondex)** — my commercial browser dungeon crawler, published through Northline Studios.
- **[Last Stop Motel](https://github.com/keepithandy/last-stop-motel)** — an offline Three.js management game with a seven-night campaign.
- **[Merge Guard](https://github.com/keepithandy/merge-guard)** — a public beta for pull-request risk analysis and targeted review checks.

## Current Focus

Right now I am focused on **Plex**: building a genuinely small coding model from scratch, training it on web-code semantics, and pairing it with deterministic repository tooling so the model can focus on planning while the surrounding system handles exact lookup, validation, and diff generation.

Alongside that research, I continue building and expanding browser games, simulation systems, fictional command interfaces, and practical developer tooling.

---

## Plex

### [Plex Nano](https://github.com/Keepithandy/plex-nano-27m-v0.0.1-p2-24)

**Repository-native coding intelligence, trained from scratch.**

Plex is a compact coding-model project built from randomly initialized weights rather than starting from a pretrained coding model. The goal is not a general chatbot; it is a focused implementation engine for understanding narrowly scoped repository tasks and producing the smallest correct change.

`PyTorch` `CUDA` `Python` `TypeScript` `HTML` `CSS` `JavaScript` `local-first`

#### Current research model

| | Current state |
|---|---|
| **Model** | Plex Nano |
| **Parameters** | 27,566,080 |
| **Context window** | 512 tokens |
| **Training** | From scratch |
| **Primary scope** | HTML, CSS, JavaScript |
| **GPU training** | CUDA |
| **CPU generation** | Working |
| **Phase** | Phase 2 — active research |

The current training direction is **Plex Web**: permissively licensed HTML/CSS/JavaScript pretraining first, followed by task-format fine-tuning for structured repository edits.

```text
TASK
  ↓
INSPECT REPOSITORY
  ↓
FIND RELEVANT FILES
  ↓
BUILD FOCUSED CONTEXT
  ↓
PLAN THE SMALLEST CORRECT EDIT
  ↓
VALIDATE
  ↓
RETURN A CLEAN DIFF
```

Plex is intentionally split into two layers:

- **Plex Nano** — semantic understanding, edit intent, target classification, structured planning, training, and evaluation.
- **Plex Code** — deterministic repository scanning, exact source resolution, validation, mutation safety, and diff generation.

> Plex is active research. The training stack and repository tooling work, but the model has not yet demonstrated reliable end-to-end general coding ability on unseen tasks.

---

### DungeonDex — Commercial Release

[**Play / Buy DungeonDex on itch.io →**](https://northline-studio.itch.io/dungeondex)

My flagship commercial browser dungeon crawler. Quick dungeon runs feed into loot, permanent gear upgrades, contracts, and persistent player records, with a mobile-first interface.

`HTML5` `JavaScript` `CSS` `dungeon crawler` `mobile-first`

#### Blender Asset Production

<img src="https://img.shields.io/badge/Blender-3D%20Asset%20Production-F5792A?logo=blender&logoColor=white" alt="Blender 3D asset production">

My 3D production work focuses on DungeonDex's gear, weapon, and item models in **Blender**, building a cohesive asset library for equipment and item presentation.

> DungeonDex is a commercial release with private source. Public builds, downloads, updates, and devlogs are available on itch.io.

---

## Featured Public Projects

### [Merge Guard](https://github.com/keepithandy/merge-guard)

A deterministic pull-request risk analyzer and targeted check planner. It highlights changed files, likely breakpoints, and useful checks for reviewers through a CLI and GitHub Action, without requiring an AI provider or API key.

**Status:** public beta — [v1.3.0-beta.2 release](https://github.com/keepithandy/merge-guard/releases/tag/v1.3.0-beta.2).

### [Last Stop Motel](https://github.com/keepithandy/last-stop-motel)

An offline, single-player Three.js management game about inheriting a roadside motel, managing guests and staff, restoring rooms, and settling the debt over seven nights. Includes campaign choices, difficulty settings, endless play, and local save import/export.

**Status:** v1.0.2. The bundled game runs locally without an account, server, or internet connection.

### [Blacksite Command](https://github.com/keepithandy/blacksite-command)

A fictional browser command-station game built around **detect → correlate → investigate → respond → contain → report**. Radar, SIGINT, satellite, and ground sources support incident decisions, while facility faults affect sensor coverage and response options.

**Status:** playable prototype with five-minute shifts, after-action reports, and a persistent local case archive.

### [GuildMasters](https://github.com/keepithandy/GuildMasters)

A fantasy guild-management strategy game with hero recruitment, contracts, crafting, guildhall growth, faction routes, and tactical encounters. Versioned saves, recovery tools, guided onboarding, and desktop/mobile navigation support the long-term progression loop.

**Status:** v2.0.0-rc.5 release candidate, with final QA and polish ahead of v2.0.0.

---

## Reusable Foundations

### [Pulse Engine](https://github.com/keepithandy/Pulse-Engine)

A framework-independent JavaScript simulation engine for deterministic, event-driven worlds. Its scope covers state, actions, rules, scheduling, seeded randomness, snapshots, persistence, and diagnostic traces.

**Status:** pre-alpha; architecture and implementation are tracked through repository issues and pull requests.

---

## What I Build With

<p align="center">
  <strong>Python · PyTorch · CUDA · JavaScript · TypeScript · HTML/CSS · React · Three.js · GitHub Actions · Blender</strong>
</p>

I like projects with a narrow purpose, explicit state, measurable progress, and enough structure to keep expanding without losing control of the system — whether that means training a tiny model, building a deterministic tool, or designing a long-running game loop.

---

## Find My Work

**Coding-model research:** [Plex Nano on GitHub](https://github.com/Keepithandy/plex-nano-27m-v0.0.1-p2-24)  
**Commercial games:** [Northline Studios on itch.io](https://northline-studio.itch.io/)  
**Development:** browse the public repositories linked above.

<sub>Profile focused on current work · updated October 6, 2026</sub>
