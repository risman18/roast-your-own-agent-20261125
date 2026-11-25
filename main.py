#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes exactly one line of text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

LINE = "My agent turned a $5 roast into a forty-step plan, three approval rounds, and a token bill bigger than the prize."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> None:
    """Enforce the competition's entry contract before writing.

    The entry must be exactly one line of 1-200 characters, valid UTF-8,
    and contain no line breaks — otherwise the submission would be
    rejected by the judge, so fail loudly here instead of writing
    a bad file silently.
    """
    line.encode("utf-8")  # raises UnicodeEncodeError on invalid characters
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200-char limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no line breaks)")


def main() -> None:
    validate_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
