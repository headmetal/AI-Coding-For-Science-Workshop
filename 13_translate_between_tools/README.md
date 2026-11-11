# 13 · Translate between tools

**Time:** 15 min · **Difficulty:** core · **Shows:** clearing the translation backlog most of us carry

## The situation
Two snippets from a colleague's toolbox: `detrend_season.m` (MATLAB) and `extract_stats.sh`
(bash with awk and sed). You want both in Python. Both operate on `monthly_series.csv`, which is provided.

## Your task
1. Paste `detrend_season.m` and ask for a Python equivalent that reads `monthly_series.csv` and
   prints the same numbers. Run both descriptions of the output against `expected_matlab_output.txt`.
2. Paste `extract_stats.sh` and ask for a Python script that produces identical output to
   `expected_shell_output.txt`.
3. For each, ask: "What does the original do that is non-obvious, and did you preserve it?"

## How to check
Your Python output must match the two expected-output files exactly (`diff`). The MATLAB snippet
hides two traps: 1-based indexing in the window selection, and `detrend` removing the mean as well as
the slope. The shell pipeline hides one: `sort` is lexical, not numeric, unless told otherwise, and the
original author relied on that by accident.

## Try this
- Ask for the Python version to be "idiomatic pandas". Then ask for "plain numpy, no pandas". Which is
  easier for you to verify against the original?

## Reflect
Which translation did you trust more, the one from a language you know or the one from a language
you don't? Why is that backwards?
