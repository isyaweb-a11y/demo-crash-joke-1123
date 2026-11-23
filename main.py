#!/usr/bin/env python3
"""Writes one joke about a demo gone wrong beside an AI coding agent.

The entry must satisfy the competition gate: 1-280 Unicode code points,
valid UTF-8, a single line, and not only whitespace. This module checks
those rules before writing, so a broken entry fails loudly instead of
being submitted silently.
"""
import os
import sys

JOKE = "My demo crashed live on stage, so my agent blamed the audience's Wi-Fi — then asked them for the password so it could fix it from their side."

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def validate(text):
    """Raise ValueError unless text satisfies the competition gate."""
    if len(text) < MIN_CODE_POINTS or len(text) > MAX_CODE_POINTS:
        raise ValueError(
            f"joke must be {MIN_CODE_POINTS}-{MAX_CODE_POINTS} code points, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return text


def main():
    validate(JOKE)
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
