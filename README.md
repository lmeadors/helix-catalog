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

## Understanding snapshots

If you're new to Helix, the `snapshot0`–`snapshot7` keys under `data.tone` in
every `.hlx` file can be confusing. A preset isn't just one fixed signal
chain — it can hold up to 8 "snapshots," saved variations of that preset's
state that you recall instantly with a footswitch, with no audio dropout and
no reloading the chain.

Per block, a snapshot can capture:

- **Bypass state** — a block can be off in one snapshot (e.g. delay off for
  a rhythm tone) and on in another (delay on for a lead tone).
- **Individual parameter values** — specific knobs can be marked
  "snapshot-controlled," so their value changes per snapshot (e.g. a drive
  knob that's lower for rhythm, higher for lead), while every other knob on
  that same block stays fixed regardless of which snapshot is active.

In HX Edit, a snapshot-controlled parameter's value is shown in
`[brackets]` rather than plain text — that's the tell for "this differs by
snapshot" vs. "this is fixed across the whole preset."

## Using the parser

```
python3 scripts/parse_hlx.py presets/samples/Randy_Tribute.hlx
```

Prints the full signal chain for each DSP path, in position order, with all
parameters for each block.

## Writing tone write-ups

A preset's companion `.flow.md` can include a "Why this tone works" section
connecting its block/parameter choices to the musical goal it's built for.
Keep these consistent across presets:

- **Voice** — write like an experienced session player explaining their
  choices to a bandmate: practical, direct, assumes some gear literacy but
  not encyclopedic knowledge. Not a fictional character, just a consistent
  register, so write-ups read like one project rather than a pile of
  one-off notes.
- **Confirmed vs. speculative** — ground each point in an actual
  `@position`/parameter value where you can, and flag anything that's
  genre convention or general gear knowledge rather than something read
  out of the JSON. One italic disclaimer at the top of the section covers
  this — no need to hedge every sentence.
- **Guitar/pickup pairing** — fine to note what guitar or pickup type
  (passive vs. active, humbucker vs. single-coil) suits a tone, since
  pickup character interacts directly with drive and amp headroom. Keep it
  at that level of generality, not specific guitar models — that's about
  as far as genre-convention advice can be defended.

## Contributing

Drop a `.hlx` file into `presets/samples/`, run it through the parser, and
open a PR — ideally noting anything you can confirm or correct in the
glossary from the actual device/HX Edit UI while you're at it.
