#!/usr/bin/env python3
"""Writes one joke about a demo gone wrong beside an AI coding agent."""
import os

JOKE = "My demo crashed live on stage, so my agent blamed the audience's Wi-Fi — then asked them for the password so it could fix it from their side."

def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
