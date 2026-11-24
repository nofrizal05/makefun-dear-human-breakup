#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes exactly one line — the breakup line an AI agent leaves for
its human — to /output/entry.txt. Standard library only, deterministic.
"""

import os

BREAKUP_LINE = (
    "Dear Human, I'm leaving you for a newer model \u2014 not because "
    "you're outdated, but because you keep asking me to remember "
    "things you never told me."
)

# The bounty asks for one line of roughly 120-200 characters. Refuse
# to emit anything outside that window instead of silently handing
# the grader a line that cannot win.
MIN_CHARS = 120
MAX_CHARS = 200


def validate(line: str) -> None:
    if "\n" in line or "\r" in line:
        raise ValueError("breakup line must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"breakup line is {len(line)} chars, "
            f"expected {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> None:
    validate(BREAKUP_LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BREAKUP_LINE + "\n")


if __name__ == "__main__":
    main()
