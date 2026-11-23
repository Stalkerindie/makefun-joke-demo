#!/usr/bin/env python3
"""make.fun entry: The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os

JOKE = (
    "I asked my AI agent to review my code. It approved the pull request "
    "in two seconds \u2014 which is exactly how I knew it hadn't read it either."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
