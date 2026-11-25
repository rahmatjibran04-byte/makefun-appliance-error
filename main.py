#!/usr/bin/env python3
"""The Funniest Honest Appliance Error - make.fun entry.

A fridge whose cooling has failed reports the truth, flatly:
the light still works, the cooling does not.

Writes exactly one line (101 characters) to /output/entry.txt.
No network, no input files, no side effects beyond that file.
"""

import os

ENTRY = "Error: The light works. The cooling does not. I am now a very expensive cupboard with a light inside."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the bounty gate before anything is written."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and prove the file holds exactly the validated line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise RuntimeError("read-back mismatch: /output/entry.txt != ENTRY")


if __name__ == "__main__":
    main()
