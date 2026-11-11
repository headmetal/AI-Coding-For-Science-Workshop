# 01 · Fix the crash

**Time:** 10–15 min · **Difficulty:** warm-up · **Shows:** debugging with and without context

## The situation
`process_sst.py` is meant to compute the annual-mean sea surface temperature anomaly for year 1 of a
10-year synthetic record and print a short summary. It currently crashes.

## Your task
1. Run it: `python process_sst.py`. Read the error.
2. Paste the **whole script and the full error message** into your AI tool and ask it to fix the crash.
3. Run the fixed version. If it crashes again, repeat. Keep count of how many rounds it takes.
4. When it finally runs, read the output. Does it look right? Check the two expected values below.

## How to check
When fully correct the script prints:
- `Year 1 global mean SST: 18.0 degC` (anything from 17.9 to 18.1 is fine)
- `Year 1 anomaly: -0.45 degC` (anything from -0.48 to -0.42 is fine; year 1 is the coolest year of a
  warming record, so a negative anomaly is expected)

If either number is outside its range, the script runs but is still wrong. There are **four** bugs in
total: two crash, two don't.

## Try this
- First ask only "fix this error". Then start again and ask "fix this error, and check the rest of the
  script for anything that would give a wrong answer without crashing". Compare what you get.
- Ask the AI to explain each bug in one sentence. Do the explanations match what you see in the code?

## Reflect
Part 1 said the model has no situational awareness. Which bug needed information that was not in the
error message? Where did that information have to come from?
