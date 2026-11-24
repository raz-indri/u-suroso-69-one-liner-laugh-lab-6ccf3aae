#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the robot vacuum's excuse after eating a sock.

The vacuum speaks like an overzealous security guard: the sock was
trespassing, and house rules are house rules.
"""

import os
import sys

LINE = (
    "In my defense, the sock was trespassing on the floor, "
    "and I enforce a zero-tolerance policy on laundry."
)

MAX_CHARS = 200


def self_check(line: str) -> None:
    """Gate check, mirroring the sealed scorer: 1-200 chars, one line."""
    text = line.strip()
    if not text:
        sys.exit("entry is empty")
    if "\n" in text:
        sys.exit("entry must be a single line")
    if len(text) > MAX_CHARS:
        sys.exit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    self_check(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE.strip() + "\n")


if __name__ == "__main__":
    main()
