#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge -- round 2 entry.

Writes one passive-aggressive note from a smart fridge to its owner
into /output/entry.txt. Python standard library only, fully
deterministic, no network access and no temporary files.
"""

import os

NOTE = "I have entered power-saving mode. Not to save power. To save myself from this conversation."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = NOTE
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry length outside the 1-200 character gate: %d" % len(text))
    if text.strip() == "" or "\n" in text or "\r" in text:
        raise SystemExit("entry must be one non-blank line")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
