# Helix Tone & Block Catalog

A community-built reference for Line 6 Helix preset files (`.hlx`). Line 6
doesn't publish an official block-model reference, and `.hlx` files —
despite the odd extension — are just plain JSON. This project decodes them:
what each block model actually does, how real presets chain blocks together,
and why.

## Why this exists

HX Edit lets you *use* Helix presets. It doesn't explain *how they're built*
or *what a given block model actually models*. This catalog is built by
opening `.hlx` files as text, tracing the signal chain, and cross-checking
uncertain parameters against the HX Edit UI to confirm what they mean.

## Structure

```
glossary/       — block model reference (what HD2_AmpBritPlexiJump etc. actually are)
presets/samples/ — .hlx files that have been dissected, used as worked examples
scripts/        — parse_hlx.py and future tooling for extracting chain data
site/           — (planned) static site generator output, public-facing catalog
```

## Status

Early. The glossary in `glossary/models.md` uses a confidence marker system:

- ✅ confirmed against the HX Edit UI
- 🟡 inferred from the JSON structure, not yet confirmed
- ❓ unknown / unidentified

Most entries are currently 🟡. Contributions that move entries to ✅ (by
checking the real UI) or add new 🟡 entries (by dissecting a new preset) are
both useful.

## Using the parser

```
python3 scripts/parse_hlx.py presets/samples/Randy_Tribute.hlx
```

Prints the full signal chain for each DSP path, in position order, with all
parameters for each block.

## Contributing

Drop a `.hlx` file into `presets/samples/`, run it through the parser, and
open a PR — ideally noting anything you can confirm or correct in the
glossary from the actual device/HX Edit UI while you're at it.
