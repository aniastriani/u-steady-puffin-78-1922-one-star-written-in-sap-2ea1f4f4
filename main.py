#!/usr/bin/env python3
"""One Star, Written in Sap.

A houseplant leaves a one-star review of the human who owns it, and the
program writes that single line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The plant's grievance: its human bought a moisture meter, consults it
every morning, and then waters the plant anyway. The plant has been
drowning since March in a pot with no drainage hole while the human
tells guests it is thriving. The joke is the gap between the gadget,
the ritual, and the puddle.

Pure standard library only; deterministic: the same bytes every run.
"""

import os
import sys

MAX_CHARS = 279

LINE = (
    "One star. He bought a moisture meter, checks it every morning, "
    "then waters me anyway \u2014 I have been drowning in a pot with no "
    "drainage hole since March while he tells his guests I am thriving."
)


def fits_gate(text):
    """The sealed gate: UTF-8 text of 1 to 279 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main():
    if not fits_gate(LINE):
        print(
            "entry does not fit the gate: %d chars" % len(LINE),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
