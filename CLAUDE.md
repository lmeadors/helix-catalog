# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A community reference for Line 6 Helix preset files (`.hlx`). Despite the extension, `.hlx` files are plain JSON. The project decodes what each block model (`@model` values like `HD2_AmpBritPlexiJump`) actually does by dissecting real presets and cross-checking against the HX Edit UI.

## Commands

Run the parser against a sample preset to print its signal chain:

```
python3 scripts/parse_hlx.py presets/samples/Randy_Tribute.hlx
```

No build, lint, or test tooling exists yet — this is a single-script, no-dependency Python 3 project (stdlib only: `json`, `sys`, `pathlib`).

## Structure

```
glossary/        — block model reference (glossary/models.md)
presets/samples/ — .hlx files that have been dissected, used as worked examples
scripts/         — parse_hlx.py and future extraction tooling
site/            — (planned) static site generator output, currently empty
```

## `.hlx` file structure

Top-level JSON keys: `version`, `meta`, `data`, `schema`. The signal chain lives at `data.tone`, under DSP path keys:

- `dsp0` / `dsp1` — "Path 1" / "Path 2". Each can internally split into parallel A/B sub-paths via structural blocks (`split`/`join`).
- Also present under `data.tone`: `snapshot0`–`snapshot7`, `controller`, `variax`, `dt0`/`dt1`/`dtdual`, `powercab0`/`powercab1`/`powercabdual`, `global`, `footswitch` — not yet parsed by `scripts/parse_hlx.py`.

Within a DSP path, each block is a dict keyed by an internal name (e.g. `"amp1"`), containing:

- `@model` — the block model identifier, e.g. `HD2_AmpBritPlexiJump`. This is the key the glossary is organized around.
- `@position` — order in the chain (used to sort blocks for display).
- `@enabled` — bypass state.
- Non-`@`-prefixed keys — the block's actual parameters (e.g. `Gain`, `Bass`, `Mix`), values in whatever units HX Edit uses (often dB, Hz, or 0–1 normalized).

`STRUCTURAL_KEYS` in `parse_hlx.py` (`inputA`, `inputB`, `outputA`, `outputB`, `split`, `join`) marks routing nodes that aren't audible effect blocks and are excluded from the printed chain — but they still carry meaningful parameters and are separately documented in the glossary under "Routing / structural".

## Glossary conventions (`glossary/models.md`)

Every block model entry carries a confidence marker — preserve this system when adding or editing entries:

- ✅ confirmed against the HX Edit UI
- 🟡 inferred from JSON structure only, not yet confirmed
- ❓ unknown / unidentified

Most entries are currently 🟡. When adding a new model, group it under the matching category heading (Dynamics, Drive, Filter / Wah, EQ, Modulation, Delay, Pitch, Amps, Cabs, Routing / structural) and list observed parameters with their apparent meaning/units. If a parameter's meaning or UI mapping is genuinely uncertain, add it to the "Open questions for HX Edit verification" section rather than guessing silently.

## Memory & error tracking

This repo tracks its own memory and error log in-repo instead of the global `~/.claude/.../memory/` auto-memory system:
- `MEMORY.md` — durable facts about the user, feedback on working style, project context, and references. Write here instead of the home-directory memory store when working in this repo.
- `ERRORS.md` — defects found in skills/code and notable runtime failures, so they aren't silently rediscovered.

## Contributing workflow

To add a new dissected preset: drop the `.hlx` file into `presets/samples/`, run it through `scripts/parse_hlx.py` to inspect its chain, and update `glossary/models.md` with any new or newly-confirmed block models found.
