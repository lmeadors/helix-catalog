#!/usr/bin/env python3
"""
parse_hlx.py — extract a readable signal chain breakdown from a Line 6 Helix
.hlx preset file (which is plain JSON under the hood).

Usage:
    python3 parse_hlx.py path/to/preset.hlx
"""

import json
import sys
from pathlib import Path

# DSP path keys as they appear in the JSON. Helix presets can have up to two
# paths (dsp0 = "Path 1", dsp1 = "Path 2"), each of which can internally
# split into A/B sub-paths via split/join structural blocks.
DSP_KEYS = ["dsp0", "dsp1"]

# Structural (non-audible) block keys that aren't part of the visible
# effects chain but define routing.
STRUCTURAL_KEYS = {"inputA", "inputB", "outputA", "outputB", "split", "join"}


def load_preset(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def describe_dsp_path(dsp: dict, label: str) -> None:
    """Print the block chain for a single DSP path, ordered by @position then @path."""
    audible_blocks = [
        (key, block)
        for key, block in dsp.items()
        if key not in STRUCTURAL_KEYS and isinstance(block, dict) and "@position" in block
    ]
    # Some blocks (e.g. a dual-mic cab's second mic, seen as a "cab0" key)
    # carry a real @model but no @position at all, so the position-ordered
    # loop below would silently skip them. Surface those separately rather
    # than losing them.
    unpositioned_blocks = [
        (key, block)
        for key, block in dsp.items()
        if key not in STRUCTURAL_KEYS and isinstance(block, dict) and "@model" in block and "@position" not in block
    ]
    # @path (0/1) picks out which parallel A/B sub-path a block sits on after
    # a split. Blocks on different sub-paths can share the same @position, so
    # sort on @path too or the two branches interleave arbitrarily.
    audible_blocks.sort(key=lambda kv: (kv[1]["@position"], kv[1].get("@path", 0)))

    # A position shared by more than one block means a split is active at
    # that point in the chain — tag those blocks with their A/B path so it's
    # clear they're parallel, not sequential.
    position_counts = {}
    for _, block in audible_blocks:
        position_counts[block["@position"]] = position_counts.get(block["@position"], 0) + 1

    print(f"\n{label}")
    print("-" * len(label))
    for key, block in audible_blocks:
        model = block.get("@model", "UNKNOWN_MODEL")
        enabled = block.get("@enabled", True)
        state = "on " if enabled else "OFF"
        pos = block.get("@position")
        pos_label = str(pos)
        if position_counts[pos] > 1:
            path = block.get("@path", 0)
            pos_label += "AB"[path] if path in (0, 1) else "?"
        # Collect the "real" params — skip the @-prefixed structural fields.
        params = {k: v for k, v in block.items() if not k.startswith("@")}
        print(f"  [{pos_label}] {state} {model}  ({key})")
        for pname, pval in params.items():
            print(f"        {pname}: {pval}")

    for key, block in unpositioned_blocks:
        model = block.get("@model", "UNKNOWN_MODEL")
        enabled = block.get("@enabled", True)
        state = "on " if enabled else "OFF"
        params = {k: v for k, v in block.items() if not k.startswith("@")}
        print(f"  [no position] {state} {model}  ({key})")
        for pname, pval in params.items():
            print(f"        {pname}: {pval}")


def describe_preset(preset: dict) -> None:
    meta = preset.get("data", {}).get("meta", {})
    name = meta.get("name", "(unnamed)")
    author = meta.get("author", "?")
    band = meta.get("band")

    print(f"Preset: {name}")
    print(f"Author: {author}")
    if band:
        print(f"Inspired by / band: {band}")

    tone = preset.get("data", {}).get("tone", {})
    for dsp_key in DSP_KEYS:
        if dsp_key in tone:
            describe_dsp_path(tone[dsp_key], f"Path: {dsp_key}")

    # Flag anything under the tone that isn't a recognized section, in case
    # the file has structure we haven't accounted for yet (variax, dt0/dt1,
    # powercab, etc.) — useful as a prompt to extend this script.
    known_prefixes = ("dsp", "snapshot", "controller", "global", "footswitch")
    unhandled = [k for k in tone.keys() if not k.startswith(known_prefixes)]
    if unhandled:
        print(f"\n(Not yet parsed by this script: {unhandled})")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 parse_hlx.py path/to/preset.hlx")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    preset = load_preset(str(path))
    describe_preset(preset)


if __name__ == "__main__":
    main()
