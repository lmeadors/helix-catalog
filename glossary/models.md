# Helix Block Model Glossary (seed)

Status legend: ✅ confirmed (against the HX Edit UI, or the official *Helix LT 3.80 Owner's Manual* / *HX Edit 3.80 Pilot's Guide*, cited inline as "Manual p.N" / "Pilot's Guide p.N") · 🟡 inferred, unconfirmed · ❓ unknown

## Dynamics
- **HD2_GateNoiseGate** ✅ — "Noise Gate." Line 6 Original (Manual p.30). Params seen: `Threshold` (dB, negative), `Decay`, `Level`.
- **HD2_CompressorLAStudioComp** ✅ — "LA Studio Comp." Based on the Teletronix LA-2A (Manual p.30). Params: `PeakReduction`, `Gain`, `Mix`, `Emphasis`, `Type` (bool — "Compress/Limit" toggle, confirmed in UI).
- **HD2_CompressorDeluxeComp** ✅ — "Deluxe Comp." Line 6 Original (Manual p.30) — explains its more modern, non-vintage param set vs. the LA Studio Comp. Params: `Threshold` (dB), `Ratio` (numeric — `0` seen, meaning/scale unconfirmed), `Attack`, `Release`, `Knee`, `Mix`, `Level`.

## Drive
- **HD2_DistScream808** ✅ — "Scream 808." Ibanez TS808 Tube Screamer (Manual p.29). Params: `Gain`, `Tone`, `Level`.
- **HD2_DistKinkyBoost** ✅ — "Kinky Boost." Based on the Xotic EP Booster (Manual p.29) — a clean-boost pedal, not a distortion, which explains why it's seen used with `Drive: 0`/`Boost: True` (as a pure level boost). Params: `Drive`, `Bright` (bool — bright-cap toggle), `Boost` (bool — separate boost stage on/off).
- **HD2_DistTeemah** ✅ — "Teemah!" Based on the Paul Cochrane Timmy Overdrive (Manual p.29). Params: `Gain`, `Bass`, `Treble`, `Level`, `Clipping` (numeric — clipping-mode selector, values/meaning still unconfirmed).
- **HD2_DistMinotaur** ✅ — "Minotaur." Based on the Klon Centaur (Manual p.29). Params: `Gain`, `Tone`, `Level`.
- **HD2_DistPrizeDrive** ✅ — "Prize Drive." Based on the Nobels ODR-1(bc) (Manual p.29) — not Klon-style as originally guessed. Params: `Drive`, `Level`, `Voltage` (bool), `Spectrum` (numeric — tone/voicing control), `Bass Cut` (bool).

## Filter / Wah
- **HD2_WahWeeper** ✅ — "Weeper." Based on the Arbiter Cry Baby (Manual p.34) — not Vox-style as originally guessed. Params: `Pedal` (position), `FcLow`, `FcHigh` (Hz — sweep range endpoints).
- **HD2_WahChrome** ✅ — "Chrome." Based on the Vox V847 (Manual p.34). Params: `Pedal`, `FcLow`, `FcHigh`, `Mix`, `Level` — same param shape as Weeper.

## EQ
- **HD2_EQGraphic10Band** ✅ — "10 Band Graphic." Based on the MXR 10-Band Graphic EQ (Manual p.30). Params: named per frequency (`31p25Hz`...`8kHz`), each in dB.
- **HD2_EQParametric** ✅ — "Parametric." Line 6 Original (Manual p.30). 3-band parametric EQ (Low/Mid/High), each with independent `Freq`/`Gain`/`Q`, plus separate `LowCut`/`HighCut`. Params: `LowFreq`, `LowGain`, `LowQ`, `MidFreq`, `MidGain`, `MidQ`, `HighFreq`, `HighGain`, `HighQ`, `LowCut`, `HighCut`, `Level`.

## Modulation
- **HD2_Chorus** ✅ — base "Chorus." Line 6 Original (Manual p.31). Params: `Speed`, `Depth`, `Mix`, `Predelay`, `Tone`, `WaveShape`, `Spread`, `SyncSelect1`/`TempoSync1` (tempo-sync controls).
- **HD2_Chorus70sChorus** ✅ — "70s Chorus." Based on the BOSS CE-1 (Manual p.31). Extra params vs. base Chorus: `ChorusIntensity`, `VibratoDepth`, `VibratoRate`, `Mode` (bool — likely chorus/vibrato switch), `Stereo`, `Headroom`, and a second tempo-sync pair `SyncSelect2`/`TempoSync2` (independent of `SyncSelect1`/`TempoSync1` — likely syncing chorus rate and vibrato rate separately).
- **HD2_FlangerGrayFlanger** ✅ — "Gray Flanger." Based on the MXR 117 Flanger (Manual p.31). Params: `Rate`, `Manual`, `Regen`, `Width`, `Mix`, `Headroom`, `Spread`.
- **HD2_RotaryVibeRotary** 🟡 — rotary speaker sim (Leslie-style). Best candidate in the manual's Modulation tables (p.31) is **"Rotary Drum/Horn," based on the Leslie 145** — the two independent tempo-synced pairs (`SyncSelect1`/`TempoSync1` and `SyncSelect2`/`TempoSync2`) match a two-rotor (drum + horn) model better than the single-rotor "145 Rotary" entry also in that table, but the exact manual row hasn't been matched string-for-string against this block's actual UI name (which the user's own footswitch label calls `"Vibe Rotary"` — see Routing/structural section on `tone.footswitch`). Params: `Speed` (bool — fast/slow switch, not continuous), `FastSpeed`, `SlowSpeed`, `RampTime` (acceleration between speeds), `Drive`, `Blend`, `Mix`, `Level`, `Headroom`, `SyncSelect1`/`SyncSelect2`/`TempoSync1`/`TempoSync2`.
- **HD2_RetroReel** ✅ — "Retro Reel." Line 6 Original, confirmed filed under **Modulation** (Manual p.31) — resolves the earlier open question about its category (its chain-view icon matches `HD2_Chorus70sChorus`'s, which was the tell). Params: `Saturation`, `WowFluttr` (tape pitch instability), `TapeSpeed` (numeric — likely selects among standard reel speeds, e.g. 7.5/15 ips), `Texture` (numeric — grain/noise character), `LowCut`, `HighCut`, `Level`. No `Mix` param seen — may always process the full signal rather than blending wet/dry.

## Delay
- **HD2_DelaySimpleDelay** ✅ — "Simple Delay." Line 6 Original (Manual p.32). Params: `Time`, `Feedback`, `Mix`, `Scale`, `@trails` (bool — trails on/off).
- **HD2_DelayTransistorTape** ✅ — "Transistor Tape." Based on the Maestro Echoplex EP-3 (Manual p.32). Params: `Time`, `Feedback`, `Mix`, `Level`, `Scale`, `Spread`, `Headroom`, `WowFlutter` (tape-style pitch instability), `SyncSelect1`/`TempoSync1`.
- **HD2_DelayHeliosphere** ✅ — "Heliosphere." Line 6 Original (Manual p.32) — **correction**: earlier described as "Eventide-style," which was an unconfirmed guess; the manual lists it as an original Line 6 design, not modeled after specific hardware. It is a modulated delay with a built-in reverb blended into the tail. Params: `Time`, `Feedback`, `Mix`, `Level`, `Scale`, `Rate`/`Depth` (delay-signal modulation), `VerbMix`/`VerbDecay` (the blended-in reverb's own mix/decay), `Headroom`, `SyncSelect1`/`TempoSync1`.

## Pitch
- **HD2_PitchSimplePitch** ✅ — "Simple Pitch." Line 6 Original (Manual p.33). Single-voice detune/shift. Params: `Cents1`, `Interval1`, `Time1` (delay before pitched voice?), `LevelVoice1`, `PanVoice1`, `PanDry`, `Mix`.

## Reverb
- **HD2_ReverbPlateaux** ✅ — "Plateaux." Line 6 Original (Manual p.32). Includes pitch-shift voices layered into the reverb tail (shimmer-style). Params: `Decay`, `Predelay`, `Tone`, `Modulation`, `Mix`, `Level`, plus two pitch voices: `Cents1`/`Pitch1`, `Cents2`/`Pitch2`, `PitchMix` (blend of shifted voices into the reverb).
- **HD2_Reverb63Spring** ✅ — "'63 Spring" (Legacy category). Line 6 Original (Manual p.33) — not modeled after a specific Fender unit despite the "'63" naming; that's evocative, not a "Based On" credit. Params: `Decay`, `Predelay`, `LowCut`, `HighCut`, `Mix`, `Level`.
- **HD2_ReverbParticle** ✅ — "Particle Verb" (Legacy category). Line 6 Original (Manual p.33). Granular/particle reverb. Params: `Dwell`, `Condition` (numeric — grain/character selector, meaning unconfirmed), `Mix`, `Level`.
- **HD2_ReverbHxSpring** 🟡 — a newer/flagship spring reverb model, distinct from the Legacy `HD2_Reverb63Spring`. Best candidate in the manual's modern Reverb Models table (p.32) is **"Hot Springs," Line 6 Original** — the only other spring-adjacent entry — but this hasn't been confirmed as an exact match to this block's actual UI name. Params: `Dwell`, `Drip` (spring-specific "boing"/transient character), `Spring Count` (numeric — number of spring pans modeled), `LowCut`, `HighCut`, `Mix`, `Level`.

## Amps
- **HD2_AmpBritPlexiJump** ✅ — "Brit Plexi Jump." Based on the Marshall Super Lead 100, jumped channels (Manual p.36). Params: `NrmDrive` ("Normal Drive") / `BrtDrive` ("Bright Drive") — both always-visible, independent knobs (no channel-jump toggle; confirmed via UI showing both simultaneously with values matching JSON), `ChVol` ("Ch Vol"), `Bass`, `Mid`, `Treble`, `Presence`, `Master`, `Bias`, `BiasX`, `Sag`, `Hum`, `Ripple`. Value scale confirmed: raw JSON 0–1 range maps to UI 0–10 display (e.g. `Master: 1` → "10.0", `BrtDrive: 0.77` → "7.7").
  - Open: `Bright Drive`, `Normal Drive`, and `Ch Vol` render with `[bracketed]` *values* in the UI — confirmed meaning (Manual p.10, Pilot's Guide p.58-59): a controller (footswitch/EXP/MIDI/Variax knob) **or the Snapshots controller** is assigned to that parameter. Which one applies to these three specific knobs on this preset is still unconfirmed.
- **HD2_AmpMatchstickCh1** ✅ — "Matchstick Ch1." Based on the Matchless DC-30, channel 1 (Manual p.36). Params: `Ch1Drive`, `ChVol`, `Bass`, `Treble`, `Cut` (presence-cut control, distinct param from `Presence`), `Presence`, `Master`, `Bias`, `BiasX`, `Sag`, `Hum`, `Ripple` — same Bias/Sag/Hum/Ripple/BiasX cluster as the Plexi model, shared amp-sim infrastructure params (Manual p.37, "Common Amp Settings").
- **HD2_AmpInterstateZed** ✅ — "Interstate Zed." Based on the Dr. Z Route 66 (Manual p.36). Params: `Drive`, `ChVol`, `Bass`, `Mid`, `Treble`, `Presence`, `Master`, `Bias`, `BiasX`, `Sag`, `Hum`, `Ripple` — same shared amp-sim param cluster as the Plexi/Matchstick models, but only one drive knob (no jumped-channel dual-drive like the Plexi).

## Volume / Utility
- **HD2_VolPanGain** ✅ — "Gain." Line 6 Original (Manual p.34). Simple gain trim block. Params: `Gain` (dB, signed).
- **HD2_VolPanVol** ✅ — "Volume Pedal." Line 6 Original (Manual p.34). Params: `Pedal` (position), `VolumeTaper` (bool — linear vs. audio taper).

## Cabs
- **HD2_Cab4x12Greenback25** ✅ — "4x12 Greenback25." 4x12" Marshall Basketweave G12M-25 (Manual p.38). Params: `LowCut`, `HighCut` (Hz), `Distance`, `EarlyReflections`, `@mic` (mic model, 0-indexed to match the UI dropdown order — confirmed via `@mic: 0` ↔ "57 Dynamic" selected in HX Edit). This is the 16-entry **Legacy Microphone Models** list (Manual p.41-42); index → UI label → real-world mic:
  - 0 — 57 Dynamic — Shure SM57
  - 1 — 409 Dynamic — Sennheiser MD 409
  - 2 — 421 Dynamic — Sennheiser MD 421-U
  - 3 — 30 Dynamic — Heil Sound PR 30
  - 4 — 20 Dynamic — Electro-Voice RE20
  - 5 — 121 Ribbon — Royer R-121
  - 6 — 160 Ribbon — Beyerdynamic M 160
  - 7 — 4038 Ribbon — Coles 4038
  - 8 — 414 Cond — AKG C414 TLII
  - 9 — 84 Cond — Neumann KM84
  - 10 — 67 Cond — Neumann U67
  - 11 — 87 Cond — Neumann U87
  - 12 — 47 Cond — Neumann U47
  - 13 — 112 Dynamic — AKG D112
  - 14 — 12 Dynamic — AKG D12
  - 15 — 7 Dynamic — Shure SM7
- **HD2_Cab4x12Greenback20** ✅ — "4x12 Greenback20." 4x12" Marshall Basketweave G12M-20 (Manual p.38). Same param shape as Greenback25.
- **HD2_Cab4x121960T75** ✅ — "4x12 1960A T75." 4x12" Marshall 1960A cab, G12T-75 speakers (Manual p.38). Same param shape as other cabs.
- **`HD2_CabMicIr_*WithPan`** ✅ — a newer IR-based cab-block family, distinct from the `HD2_Cab4x12*` Legacy family above. Extra params vs. the Legacy cabs: `Angle` (mic angle, in addition to `Position`/`Distance`), `Pan`, `Delay` (sub-millisecond time offset — phase/time-alignment between two mics), `Mic` (numeric index, not `@`-prefixed here). Confirmed instances:
  - `HD2_CabMicIr_2x12BlueBellWithPan` — "2x12 Blue Bell": 2x12" Vox AC-30 Fawn, Blue Alnico speaker (Manual p.38).
  - `HD2_CabMicIr_2x12InterstateWithPan` — "2x12 Interstate": 2x12" Dr. Z Z Best cab, V30 speaker (Manual p.38).
  - Supports a dual-mic blend per block: the in-chain cab (`block5`, Blue Bell) carries `"@cab": "cab0"`, a direct reference to a second, positionless block (Interstate) holding the second mic's config — **confirmed against HX Edit**, whose chain view shows only one Cab icon here, not two.
  - 🟡 Mic index list: these blocks use a different, larger **Microphone Models** list (Manual p.39, Guitar category, 12 entries: 57 Dynamic, 421 Dynamic, 7 Dynamic, 906 Dynamic, 30 Dynamic, 121 Ribbon, 160 Ribbon, 4038 Ribbon, 84 Ribbon, 414 Cond, 47 Cond FET, 67 Cond) rather than the 16-entry Legacy list above. If 0-indexed in that reading order, `country stuff di.hlx`'s `Mic: 0` (Blue Bell) = 57 Dynamic (Shure SM57) and `Mic: 5` (Interstate) = 121 Ribbon (Royer R-121) — plausible but **not confirmed against an actual UI dropdown** for this block type, unlike the Legacy list which was screenshot-verified.
  - See `scripts/parse_hlx.py`'s `unpositioned_blocks` handling, added to stop `@cab`-referenced blocks like this from being silently dropped.

## Routing / structural (not audible "blocks")
- **HD2_AppDSPFlow1Input / 2Input** — path input node. `noiseGate` (bool, separate from the Gate block?), `threshold`, `decay`.
- **HD2_AppDSPFlowOutput** — path output node. `gain`, `pan`.
- **HD2_AppDSPFlowSplitY** — Y-split into parallel sub-paths (A/B). `BalanceA`/`BalanceB`. Officially called "Split" in the UI (Pilot's Guide p.31); four split types exist (Y, A/B, Crossover, Dynamic) — only Y has been seen in dissected presets so far.
- **HD2_AppDSPFlowJoin** — merge point for split paths. `A Level`/`B Level`, `A Pan`/`B Pan`, `B Polarity` (phase invert on B). Officially called "Merge" (or "Merge-Mixer") in the UI (Pilot's Guide p.30-31), not "Join" — the JSON model name is the odd one out here.
- **`@path`** ✅ — appears on blocks that sit between a split and its join; `0` = path A, `1` = path B. Blocks on parallel A/B paths can share the same `@position` value (position appears to number *slots* in the chain, not a single linear order). `scripts/parse_hlx.py` sorts on `(@position, @path)` and tags shared-position blocks with their A/B letter. Seen in `Matchless (v3).hlx`, where dsp0 splits post-amp into two parallel cabs and dsp1 splits into two parallel reverbs — **confirmed against the HX Edit signal chain view**: dsp1's split does produce a 3-block branch (Plateaux → 63 Spring → Particle) in parallel with a 1-block branch (a second Plateaux instance), rejoining before the EQ, matching what `@position`/`@path` predicted. The split/join blocks' own `@position` values still don't follow an obvious consistent rule (dsp0's `join` position was one past its parallel row; dsp1's coincided with a block on the longer branch) — doesn't matter for topology since the audible blocks' own `@position`/`@path` values are sufficient and reliable.
- **Path 1 → Path 2 series routing** 🟡 — in `Matchless (v3).hlx`, HX Edit's chain view shows dsp0 ("Path 1") taking input from "Guitar" and its output routed into "Path 2A", while dsp1 ("Path 2") shows its own input as "None" rather than a guitar feed — i.e. this preset chains Path 1 into Path 2 in series, not two independent paths both fed from the guitar. `dsp0.inputA.@input` was `2` and `dsp1.inputA.@input` was `0` in that preset; `country stuff di.hlx` shows the exact same pattern, a second data point consistent with `2` = guitar-fed, `0` = fed from elsewhere. The Owner's Manual (p.10) and Pilot's Guide (p.32) both show an input source picker with options including Guitar, Aux In, Variax, and (implicitly) None/fed-from-other-path — a lead for pinning down the exact `@input` value-to-source mapping, not yet done.
- **`@topology0`/`@topology1`** 🟡 — per-path string under `global`, e.g. `"A"` or `"SABJ"`. In `country stuff di.hlx`, dsp0 (no active split) has `@topology0: "A"`, while dsp1 (has a real split into two parallel delays) has `@topology1: "SABJ"` — reads as literally spelling out the path's structure (**S**plit, **A**, **B**, **J**oin) vs. just `"A"` for a plain single-lane path. In `Matchless (v3).hlx`, both paths have active splits and both were `"SABJ"`, consistent with this reading.
- **Base `@enabled` reflects snapshot 0** ✅ — confirmed in `country stuff di.hlx`: every block's top-level `@enabled` value matches that preset's `snapshot0` (`@name: "Clean-ish"`) bypass state exactly (`snapshotN.blocks.dspX.blockY`, a per-snapshot bool per block), and `global.@current_snapshot` was `0`. So parsing `@enabled` directly (what `parse_hlx.py` does) reports snapshot 0's bypass state specifically. Bypass can differ per snapshot — in this preset, snapshot 3 ("Lead") has three blocks flipped relative to snapshot 0.
- **`@no_snapshot_bypass`** ✅ — confirmed: this is the "Snapshot Bypass" per-block setting (Owner's Manual p.50, "Snapshot Block Bypass On/Off"). Default is `False` (bypass state is snapshot-controlled, the normal case); setting it `True` in the UI ("Off" in the block's Snapshot Bypass field) excludes that block's bypass from snapshot recall entirely, so it stays manually controlled regardless of which snapshot is active.
- **`snapshotN` structure** ✅ — `data.tone.snapshot0`–`snapshot7` (always 8, one per hardware slot). `@name`/`@custom_name` (bool — false/absent for an untouched default-named slot like `"SNAPSHOT 5"`), `blocks.dspX.blockY` (bool — per-snapshot bypass override for that block, plus a `split` key for whether the split itself is active), `controllers.dspX.blockY.ParamName.{@value, @fs_enabled}` (per-snapshot parameter override; per the Owner's Manual p.50/58, a preset can have up to 64 such controller assignments total, and this is a separate mechanism from the `tone.footswitch` bypass-assignment structure below). **Indexing gotcha**: HX Edit numbers snapshots 1–8 in the UI; the JSON key is 0-indexed, so UI slot N = JSON key `snapshotN-1`. Confirmed in `Matchless (v3).hlx`: the header showed "8 AMBIENT" and JSON key `snapshot7` (UI slot 8) has `@name: "AMBIENT"`.
- **`[bracketed]` block names in the chain view** ✅ — **solved**. Per the HX Edit Pilot's Guide (p.30, "Block Bypass Assignment Indicator"): "If you create a Bypass assignment for any Amp or Effects block within your tone (via any footswitch, EXP, or MIDI type hardware controller), you'll see the block name label displayed in brackets." This is a *different* mechanism from snapshot-controlled bypass or the `controllers` per-parameter automation — it's whether the block's on/off state is *also* mapped to a physical footswitch/expression-pedal/MIDI-CC. Confirmed directly against `country stuff di.hlx`: the top-level `tone.footswitch.dspX.blockY` object exists for exactly the 6 blocks that render bracketed in HX Edit (`[Pitch]`, `[Dist]`, `[Mod]` on dsp0; both `[Delay]`s and `[Vol]` on dsp1) and no others.
- **`tone.footswitch` structure** ✅ — top-level key (sibling of `dsp0`/`dsp1`/`global`/`snapshotN`), holding `dspX.blockY` entries only for blocks with a footswitch/EXP/MIDI bypass assignment (see above). Fields seen: `@fs_index` (numeric — which footswitch/assignment slot, `2`–`13` seen so far, range/meaning not fully mapped), `@fs_primary` (bool, present only on one block when multiple blocks share the same `@fs_index` — likely marks which one is "primary" for the "MULTIPLE (X)" label described in the Owner's Manual, p.57), `@fs_ledcolor` (numeric — likely a packed RGB value, not decoded), `@fs_momentary` (bool — momentary vs. latching footswitch behavior, Owner's Manual p.55), `@fs_enabled` (bool — unconfirmed exact meaning; plausibly whether the assignment is currently active vs. disabled-but-retained), `@fs_label` (string — the custom footswitch label text, e.g. `"Vibe Rotary"`, `"Simple Delay"`). Not yet dissected by `scripts/parse_hlx.py`.

## Sources
- *Helix LT 3.80 Owner's Manual* (`Helix LT 3.80 Owner's Manual - English .pdf`) — hardware/firmware documentation: block model tables with real-world "Based On" gear, mic lists, snapshot/bypass/controller mechanics.
- *HX Edit 3.80 Pilot's Guide* (`HX Edit Pilots Guide 3.80 - English .pdf`) — HX Edit desktop app documentation: Signal Flow window conventions (bracketed block labels, Split/Merge terminology, block indicators) not covered by the hardware manual.

## Open questions for HX Edit verification
- `HD2_DistTeemah`'s `Clipping` and `HD2_ReverbParticle`'s `Condition` are numeric params with unclear meaning — likely mode/character selectors. Need UI check of what values/labels they cycle through.
- `HD2_RotaryVibeRotary`'s `Speed` param is a bool, not continuous — confirm it's a fast/slow footswitch-style toggle rather than a knob, and that `FastSpeed`/`SlowSpeed` are the two speeds it toggles between. Also confirm its exact manual-table identity (see Modulation section).
- Confirm `HD2_ReverbHxSpring`'s real UI name/identity (candidate: "Hot Springs," see Reverb section).
- Confirm the `CabMicIr` mic index list and ordering against an actual HX Edit dropdown (only pattern-matched to the manual's table order so far, see Cabs section).
- What do `@input` values on `inputA`/`inputB` mean beyond `0`/`2`, and where/how is Path 1 → Path 2 series routing (vs. independent parallel paths) actually encoded in the JSON?
- `tone.footswitch`'s `@fs_index` range/meaning and `@fs_enabled`'s exact semantics (see Routing/structural section) — not yet dissected by the parser or cross-checked against the Bypass Assign UI screen.
