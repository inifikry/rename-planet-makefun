#!/usr/bin/env python3
"""Rename the Planet (make.fun) - entry program.

Writes one funny line to /output/entry.txt: a new name for Venus plus
the why, in a single line under 200 characters.

The joke: Venus spins so slowly that one day there lasts longer than
its whole year, so it is chronically late for everything, including
its own year.
"""

import os

LINE = (
    "Venus is now 'The Chronically Late Planet' because a single day "
    "there outlasts its entire year."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Gate check mirroring the RULES gate: 1-200 chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry is empty or whitespace only")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    if "\n" in line.rstrip("\n") or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
