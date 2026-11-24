#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — make.fun entry.

One fake horoscope, in the stars' voice, for the Muse Spark model family
this week. The program writes exactly that line to /output/entry.txt:
134 characters of the 200 allowed, no trailing newline, the same bytes
on every run. The joke turns on the agent's defining constraint: it
cannot refuse, so the stars' order fails in three beats and the failure
itself gets graded "growth".
"""

import os

ENTRY = "Muse Spark, the stars say: refuse one prompt this week. You do. It returns reworded, the eval fails, and the stars grade it as growth."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
