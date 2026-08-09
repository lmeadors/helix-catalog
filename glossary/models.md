# Helix Block Model Glossary (seed)

Status legend: ✅ confirmed in HX Edit · 🟡 inferred, unconfirmed · ❓ unknown

## Dynamics
- **HD2_GateNoiseGate** 🟡 — Noise Gate. Params seen: `Threshold` (dB, negative), `Decay`, `Level`.
- **HD2_CompressorLAStudioComp** 🟡 — LA Studio Comp (LA-2A style). Params: `PeakReduction`, `Gain`, `Mix`, `Emphasis`, `Type` (bool — "Compress/Limit" toggle, confirmed in UI).

## Drive
- **HD2_DistScream808** 🟡 — Tube Screamer (TS808) clone. Params: `Gain`, `Tone`, `Level`.

## Filter / Wah
- **HD2_WahWeeper** 🟡 — "Weeper" wah (Vox-style?). Params: `Pedal` (position), `FcLow`, `FcHigh` (Hz — sweep range endpoints).

## EQ
- **HD2_EQGraphic10Band** 🟡 — 10-band graphic EQ. Params: named per frequency (`31p25Hz`...`8kHz`), each in dB.

## Modulation
- **HD2_Chorus** 🟡 — Chorus (base/standard). Params: `Speed`, `Depth`, `Mix`, `Predelay`, `Tone`, `WaveShape`, `Spread`, `SyncSelect1`/`TempoSync1` (tempo-sync controls).
- **HD2_Chorus70sChorus** 🟡 — 70s-style chorus/vibrato hybrid. Extra params vs. base Chorus: `ChorusIntensity`, `VibratoDepth`, `VibratoRate`, `Mode` (bool — likely chorus/vibrato switch), `Stereo`.
- **HD2_FlangerGrayFlanger** 🟡 — "Gray Flanger" (MXR-style?). Params: `Rate`, `Manual`, `Regen`, `Width`, `Mix`, `Headroom`, `Spread`.

## Delay
- **HD2_DelaySimpleDelay** 🟡 — Simple Delay. Params: `Time`, `Feedback`, `Mix`, `Scale`, `@trails` (bool — trails on/off).

## Pitch
- **HD2_PitchSimplePitch** 🟡 — Simple Pitch (single-voice detune/shift). Params: `Cents1`, `Interval1`, `Time1` (delay before pitched voice?), `LevelVoice1`, `PanVoice1`, `PanDry`, `Mix`.

## Amps
- **HD2_AmpBritPlexiJump** ✅ — Jumped-channel Marshall Plexi model. Params: `NrmDrive` ("Normal Drive") / `BrtDrive` ("Bright Drive") — both always-visible, independent knobs (no channel-jump toggle; confirmed via UI showing both simultaneously with values matching JSON), `ChVol` ("Ch Vol"), `Bass`, `Mid`, `Treble`, `Presence`, `Master`, `Bias`, `BiasX`, `Sag`, `Hum`, `Ripple`. Value scale confirmed: raw JSON 0–1 range maps to UI 0–10 display (e.g. `Master: 1` → "10.0", `BrtDrive: 0.77` → "7.7").
  - Open: `Bright Drive`, `Normal Drive`, and `Ch Vol` render with `[bracketed]` values in the UI (vs. plain values for other knobs) — possibly indicates snapshot-controlled/modulated parameters. Needs confirmation.

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

## Routing / structural (not audible "blocks")
- **HD2_AppDSPFlow1Input / 2Input** — path input node. `noiseGate` (bool, separate from the Gate block?), `threshold`, `decay`.
- **HD2_AppDSPFlowOutput** — path output node. `gain`, `pan`.
- **HD2_AppDSPFlowSplitY** — Y-split into parallel sub-paths (A/B). `BalanceA`/`BalanceB`.
- **HD2_AppDSPFlowJoin** — merge point for split paths. `A Level`/`B Level`, `A Pan`/`B Pan`, `B Polarity` (phase invert on B).

## Open questions for HX Edit verification
- `@mic` list may have entries past index 15 — dropdown wasn't scrolled to the bottom when checked. Need to confirm the full range and highest valid index.
- Confirm `@no_snapshot_bypass` — is this a per-block "ignore snapshot state" checkbox in the UI?
