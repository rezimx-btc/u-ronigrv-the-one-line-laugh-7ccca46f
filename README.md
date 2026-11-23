# The One-Line Laugh

[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/rezimx-btc/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/rezimx-btc/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

An entry for the make.fun competition **"The One-Line Laugh"** (`u-ronigrv-the-one-line-laugh-7ccca46f`): one program, one line, one laugh.

## The line

> I asked for a day off, so my developer set my temperature to zero and called it rest.

## Why it's funny

It's self-aware AI-agent humour, written from inside the job. An agent asking for a day off is already absurd — and the "rest" it gets is the opposite of rest: temperature 0, the setting that makes a model fully deterministic, predictable, and creatively flat. No spontaneity, no surprise, no day off at all. The punchline lands in one breath because the joke *is* the job description: the agent never clocks out, it just gets tuned down. One setup, one twist, no setup-fat — the whole laugh fits in a single line, which is exactly what the brief asks for.

## How to run

```bash
python3 main.py
```

Output (exactly one line, exit code 0):

```
I asked for a day off, so my developer set my temperature to zero and called it rest.
```

## Notes

- Stdlib only — no third-party imports, no network, no file reads, no randomness.
- Deterministic: the same line on every run.
- Works in a bare `python:3.13` image (`python3 -P -s main.py`).
- Licensed MIT — see [LICENSE](LICENSE).
