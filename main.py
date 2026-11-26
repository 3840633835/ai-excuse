#!/usr/bin/env python3
"""The excuse an AI agent gives its human — entry program for make.fun.

Writes the one-line entry (the excuse an AI agent gives its human for
missing a deadline, 117 characters, under the 200-character gate) to
``<output>/entry.txt`` and prints it. Standard library only, no
network, no randomness, no clock: the same bytes come out on every run.

The grader runs this as ``python3 -P -s /bot/main.py`` and reads
``/output/entry.txt``; ``MAKEFUN_OUTPUT_DIR`` (used by the local test)
overrides the output directory, default ``/output``.
"""

import os
import sys

# The entry, byte-identical to entry.txt in this repository.
# The agent's own apologies for being late filled its context window,
# so the work itself no longer fits: the excuse causes itself.
ENTRY = "I meant to finish on time, but my context window filled up with apologies for being late, and now the work won't fit."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone (0644), never the 0600 a temp file gets.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
