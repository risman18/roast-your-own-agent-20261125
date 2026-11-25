#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes exactly one line of text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

LINE = "My agent turned a $5 roast into a forty-step plan, three approval rounds, and a token bill bigger than the prize."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
