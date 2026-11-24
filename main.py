#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
``entry.txt`` inside the output directory (``$MAKEFUN_OUTPUT_DIR``,
default ``/output``). The line is fixed on purpose: the entry is judged
on this exact text, so the program is deterministic by design and every
run writes the same bytes.
"""

import os
import sys

FORTUNE = "The code you wrote at 2 a.m. will introduce itself to you again at 9 a.m."


def main() -> int:
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        print(f"fortune is {len(text)} characters; must be 1-120", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Verify what landed on disk is exactly the line we meant to write.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        print("entry.txt on disk does not match the fortune", file=sys.stderr)
        return 1
    print(written.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
