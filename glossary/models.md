# Helix Block Model Glossary (seed)

Status legend: ✅ confirmed in HX Edit · 🟡 inferred, unconfirmed · ❓ unknown

## Dynamics
- **HD2_GateNoiseGate** 🟡 — Noise Gate. Params seen: `Threshold` (dB, negative), `Decay`, `Level`.
- **HD2_CompressorLAStudioComp** 🟡 — LA Studio Comp (LA-2A style). Params: `PeakReduction`, `Gain`, `Mix`, `Emphasis`, `Type` (bool — "Compress/Limit" toggle, confirmed in UI).

## Drive
- **HD2_DistScream808** 🟡 — Tube Screamer (TS808) clone. Params: `Gain`, `Tone`, `Level`.
- **HD2_DistKinkyBoost** 🟡 — "Kinky Boost" drive (Way Huge Kinky Boost?). Params: `Drive`, `Bright` (bool — bright-cap toggle), `Boost` (bool — separate boost stage on/off).
- **HD2_DistTeemah** 🟡 — "Teemah!" drive. Params: `Gain`, `Bass`, `Treble`, `Level`, `Clipping` (numeric — clipping-mode selector, values/meaning unconfirmed).
- **HD2_DistMinotaur** 🟡 — "Minotaur" drive. Params: `Gain`, `Tone`, `Level`.

## Filter / Wah
- **HD2_WahWeeper** 🟡 — "Weeper" wah (Vox-style?). Params: `Pedal` (position), `FcLow`, `FcHigh` (Hz — sweep range endpoints).
- **HD2_WahChrome** 🟡 — "Chrome" wah. Params: `Pedal`, `FcLow`, `FcHigh`, `Mix`, `Level` — same param shape as Weeper.

## EQ
- **HD2_EQGraphic10Band** 🟡 — 10-band graphic EQ. Params: named per frequency (`31p25Hz`...`8kHz`), each in dB.
- **HD2_EQParametric** 🟡 — 3-band parametric EQ (Low/Mid/High), each with independent `Freq`/`Gain`/`Q`, plus separate `LowCut`/`HighCut`. Params: `LowFreq`, `LowGain`, `LowQ`, `MidFreq`, `MidGain`, `MidQ`, `HighFreq`, `HighGain`, `HighQ`, `LowCut`, `HighCut`, `Level`.

## Modulation
- **HD2_Chorus** 🟡 — Chorus (base/standard). Params: `Speed`, `Depth`, `Mix`, `Predelay`, `Tone`, `WaveShape`, `Spread`, `SyncSelect1`/`TempoSync1` (tempo-sync controls).
- **HD2_Chorus70sChorus** 🟡 — 70s-style chorus/vibrato hybrid. Extra params vs. base Chorus: `ChorusIntensity`, `VibratoDepth`, `VibratoRate`, `Mode` (bool — likely chorus/vibrato switch), `Stereo`, `Headroom`, and a second tempo-sync pair `SyncSelect2`/`TempoSync2` (independent of `SyncSelect1`/`TempoSync1` — likely syncing chorus rate and vibrato rate separately).
- **HD2_FlangerGrayFlanger** 🟡 — "Gray Flanger" (MXR-style?). Params: `Rate`, `Manual`, `Regen`, `Width`, `Mix`, `Headroom`, `Spread`.

## Delay
- **HD2_DelaySimpleDelay** 🟡 — Simple Delay. Params: `Time`, `Feedback`, `Mix`, `Scale`, `@trails` (bool — trails on/off).
- **HD2_DelayTransistorTape** 🟡 — Transistor/solid-state tape-style delay. Params: `Time`, `Feedback`, `Mix`, `Level`, `Scale`, `Spread`, `Headroom`, `WowFlutter` (tape-style pitch instability), `SyncSelect1`/`TempoSync1`.

## Pitch
- **HD2_PitchSimplePitch** 🟡 — Simple Pitch (single-voice detune/shift). Params: `Cents1`, `Interval1`, `Time1` (delay before pitched voice?), `LevelVoice1`, `PanVoice1`, `PanDry`, `Mix`.

## Reverb
- **HD2_ReverbPlateaux** 🟡 — "Plateaux" reverb — includes pitch-shift voices layered into the reverb tail (shimmer-style). Params: `Decay`, `Predelay`, `Tone`, `Modulation`, `Mix`, `Level`, plus two pitch voices: `Cents1`/`Pitch1`, `Cents2`/`Pitch2`, `PitchMix` (blend of shifted voices into the reverb).
- **HD2_Reverb63Spring** 🟡 — '63-style spring reverb (Fender-style). Params: `Decay`, `Predelay`, `LowCut`, `HighCut`, `Mix`, `Level`.
- **HD2_ReverbParticle** 🟡 — Granular/particle reverb. Params: `Dwell`, `Condition` (numeric — grain/character selector, meaning unconfirmed), `Mix`, `Level`.

## Amps
- **HD2_AmpBritPlexiJump** ✅ — Jumped-channel Marshall Plexi model. Params: `NrmDrive` ("Normal Drive") / `BrtDrive` ("Bright Drive") — both always-visible, independent knobs (no channel-jump toggle; confirmed via UI showing both simultaneously with values matching JSON), `ChVol` ("Ch Vol"), `Bass`, `Mid`, `Treble`, `Presence`, `Master`, `Bias`, `BiasX`, `Sag`, `Hum`, `Ripple`. Value scale confirmed: raw JSON 0–1 range maps to UI 0–10 display (e.g. `Master: 1` → "10.0", `BrtDrive: 0.77` → "7.7").
  - Open: `Bright Drive`, `Normal Drive`, and `Ch Vol` render with `[bracketed]` values in the UI (vs. plain values for other knobs) — possibly indicates snapshot-controlled/modulated parameters. Needs confirmation.
- **HD2_AmpMatchstickCh1** 🟡 — "Matchstick" (Matchless DC-30-style) amp model, Channel 1. Params: `Ch1Drive`, `ChVol`, `Bass`, `Treble`, `Cut` (presence-cut control, distinct param from `Presence`), `Presence`, `Master`, `Bias`, `BiasX`, `Sag`, `Hum`, `Ripple` — same Bias/Sag/Hum/Ripple/BiasX cluster as the Plexi model, likely shared amp-sim infrastructure params.

## Volume / Utility
- **HD2_VolPanGain** 🟡 — simple gain trim block. Params: `Gain` (dB, signed).
- **HD2_VolPanVol** 🟡 — volume pedal block. Params: `Pedal` (position), `VolumeTaper` (bool — linear vs. audio taper).

## Cabs
- **HD2_Cab4x12Greenback25** ✅ — 4x12 cab loaded with Greenback 25 speakers. Params: `LowCut`, `HighCut` (Hz), `Distance`, `EarlyReflections`, `@mic` (mic model, 0-indexed to match the UI dropdown order — confirmed via `@mic: 0` ↔ "57 Dynamic" selected in HX Edit). Mic list, index → UI label:
  - 0 — 57 Dynamic
  - 1 — 409 Dynamic
  - 2 — 421 Dynamic
  - 3 — 30 Dynamic
  - 4 — 20 Dynamic
  - 5 — 121 Ribbon
  - 6 — 160 Ribbon
  - 7 — 4038 Ribbon
  - 8 — 414 Cond
  - 9 — 84 Cond
  - 10 — 67 Cond
  - 11 — 87 Cond
  - 12 — 47 Cond
  - 13 — 112 Dynamic
  - 14 — 12 Dynamic
  - 15 — 7 Dynamic
  (List may continue past index 15 — dropdown was scrollable and not scrolled to bottom in the checked screenshot.)
- **HD2_Cab4x12Greenback20** 🟡 — 4x12 cab loaded with Greenback 20 speakers. Same param shape as Greenback25: `LowCut`, `HighCut`, `Distance`, `EarlyReflections`, `Level`, `@mic`.
- **HD2_Cab4x121960T75** 🟡 — Marshall 1960T-style 4x12 loaded with Celestion G12T-75 speakers. Same param shape as other cabs.

## Routing / structural (not audible "blocks")
- **HD2_AppDSPFlow1Input / 2Input** — path input node. `noiseGate` (bool, separate from the Gate block?), `threshold`, `decay`.
- **HD2_AppDSPFlowOutput** — path output node. `gain`, `pan`.
- **HD2_AppDSPFlowSplitY** — Y-split into parallel sub-paths (A/B). `BalanceA`/`BalanceB`.
- **HD2_AppDSPFlowJoin** — merge point for split paths. `A Level`/`B Level`, `A Pan`/`B Pan`, `B Polarity` (phase invert on B).
- **`@path`** ✅ — appears on blocks that sit between a split and its join; `0` = path A, `1` = path B. Blocks on parallel A/B paths can share the same `@position` value (position appears to number *slots* in the chain, not a single linear order). `scripts/parse_hlx.py` sorts on `(@position, @path)` and tags shared-position blocks with their A/B letter. Seen in `Matchless (v3).hlx`, where dsp0 splits post-amp into two parallel cabs and dsp1 splits into two parallel reverbs — **confirmed against the HX Edit signal chain view**: dsp1's split does produce a 3-block branch (Plateaux → 63 Spring → Particle) in parallel with a 1-block branch (a second Plateaux instance), rejoining before the EQ, matching what `@position`/`@path` predicted. The split/join blocks' own `@position` values still don't follow an obvious consistent rule (dsp0's `join` position was one past its parallel row; dsp1's coincided with a block on the longer branch) — doesn't matter for topology since the audible blocks' own `@position`/`@path` values are sufficient and reliable.
- **Path 1 → Path 2 series routing** 🟡 — in `Matchless (v3).hlx`, HX Edit's chain view shows dsp0 ("Path 1") taking input from "Guitar" and its output routed into "Path 2A", while dsp1 ("Path 2") shows its own input as "None" rather than a guitar feed — i.e. this preset chains Path 1 into Path 2 in series, not two independent paths both fed from the guitar. `dsp0.inputA.@input` was `2` and `dsp1.inputA.@input` was `0` in this preset; haven't yet worked out what `@input`'s possible values mean in general (guitar vs. aux vs. "fed from the other path" etc.) or where the series-vs-parallel routing mode is actually stored in the JSON. Needs a preset with a different topology (e.g. two genuinely parallel paths) to compare against.

## Open questions for HX Edit verification
- `@mic` list may have entries past index 15 — dropdown wasn't scrolled to the bottom when checked. Need to confirm the full range and highest valid index.
- Confirm `@no_snapshot_bypass` — is this a per-block "ignore snapshot state" checkbox in the UI?
- What do `@input` values on `inputA`/`inputB` mean (0, 2 seen so far), and where/how is Path 1 → Path 2 series routing (vs. independent parallel paths) actually encoded in the JSON?
- `HD2_DistTeemah`'s `Clipping` and `HD2_ReverbParticle`'s `Condition` are numeric params with unclear meaning — likely mode/character selectors. Need UI check of what values/labels they cycle through.
