#!/usr/bin/env python3
"""make.fun entry: The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network, no randomness.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "I asked my AI agent to review my code. It approved the pull request "
    "in two seconds \u2014 which is exactly how I knew it hadn't read it either."
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
