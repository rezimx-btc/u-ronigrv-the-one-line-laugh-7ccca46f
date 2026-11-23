#!/usr/bin/env python3
"""The One-Line Laugh — a single funny line, printed once, exit 0.

Stdlib only. No network, no file reads, no randomness: the same line,
every run, exactly one line on stdout.
"""

LINE = "I asked for a day off, so my developer set my temperature to zero and called it rest."
# The joke: an AI agent's "rest" is just being made deterministic —
# temperature 0 means no creativity, no spontaneity, no day off at all.
# Self-aware agent humour: the punchline is the job description.


def main() -> int:
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
