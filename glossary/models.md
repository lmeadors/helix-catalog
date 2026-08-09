# Helix Block Model Glossary (seed)

Status legend: ✅ confirmed in HX Edit · 🟡 inferred, unconfirmed · ❓ unknown

## Dynamics
- **HD2_GateNoiseGate** 🟡 — Noise Gate. Params seen: `Threshold` (dB, negative), `Decay`, `Level`.
- **HD2_CompressorLAStudioComp** 🟡 — LA Studio Comp (LA-2A style). Params: `PeakReduction`, `Gain`, `Mix`, `Emphasis`, `Type` (bool — likely compressor/limiter mode toggle, unconfirmed).

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
- **HD2_AmpBritPlexiJump** 🟡 — Jumped-channel Marshall Plexi model. Params: `NrmDrive`/`BrtDrive` (normal/bright channel gains — relationship to UI unconfirmed), `ChVol`, `Bass`, `Mid`, `Treble`, `Presence`, `Master`, `Bias`, `BiasX`, `Sag`, `Hum`, `Ripple`.

## Cabs
- **HD2_Cab4x12Greenback25** 🟡 — 4x12 cab loaded with Greenback 25 speakers. Params: `LowCut`, `HighCut` (Hz), `Distance`, `EarlyReflections`, `@mic` (mic model index — needs mic ID→name mapping).

## Routing / structural (not audible "blocks")
- **HD2_AppDSPFlow1Input / 2Input** — path input node. `noiseGate` (bool, separate from the Gate block?), `threshold`, `decay`.
- **HD2_AppDSPFlowOutput** — path output node. `gain`, `pan`.
- **HD2_AppDSPFlowSplitY** — Y-split into parallel sub-paths (A/B). `BalanceA`/`BalanceB`.
- **HD2_AppDSPFlowJoin** — merge point for split paths. `A Level`/`B Level`, `A Pan`/`B Pan`, `B Polarity` (phase invert on B).

## Open questions for HX Edit verification
- Does `@mic` on cab blocks correspond to a visible dropdown list we can map fully (0 = ?, 1 = ?, etc.)?
- Is `NrmDrive` vs `BrtDrive` on the Plexi model two independent visible knobs, or does the UI show one depending on a channel-jump toggle?
- What does `Type` (bool) do on LA Studio Comp — visible mode switch?
- Confirm `@no_snapshot_bypass` — is this a per-block "ignore snapshot state" checkbox in the UI?
