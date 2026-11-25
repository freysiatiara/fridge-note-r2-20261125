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
    # Post-write verification: the file on disk must be exactly the entry
    # text, one line, and mode 0644 — otherwise fail loudly instead of
    # shipping a corrupt or unreadable output.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("post-write verification failed: output differs from entry text")
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("post-write verification failed: output mode is not 0644")


if __name__ == "__main__":
    main()
