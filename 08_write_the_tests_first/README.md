# 08 · Write the tests first

**Time:** 15 min · **Difficulty:** core · **Shows:** the AI checking the human, instead of the other way round

## The situation
`running_mean.py` holds a function a colleague wrote and has used for years. It smooths a 1-D series
with a centred running mean. It "works".

## Your task
1. Paste only the function and ask the AI to write a set of tests for it using plain `assert`
   statements (no pytest needed), **including edge cases the author may not have thought of**.
   Do not ask it to look for bugs yet.
2. Save the tests as `test_running_mean.py` and run them: `python test_running_mean.py`.
3. Some tests will fail. For each failure, decide: is the **test** wrong or is the **function** wrong?
   Ask the AI to argue each case, then decide yourself.
4. Fix the function. Re-run.

## How to check
A good test set probes at least: the edges of the series, an even window length, NaN in the input,
a window longer than the series, a window of 1, and a constant series. At least two of those expose
genuine problems in the function.

## Try this
- Ask the AI to write the tests *before* it sees the function, from the one-line description
  "a centred running mean of a 1-D numpy array with a given odd window". Which set of tests is better?

## Reflect
This reverses the usual relationship. Did you trust the AI more or less as a checker than as a writer?
