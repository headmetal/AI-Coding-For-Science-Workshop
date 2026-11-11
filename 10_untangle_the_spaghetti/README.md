# 10 · Untangle the spaghetti

**Time:** 20 min · **Difficulty:** core · **Shows:** refactoring, and making the AI prove equivalence

## The situation
`spaghetti.py` is a real-world style analysis script: globals everywhere, three near-identical copies
of the same block, magic numbers, prints mixed with computation. It works. Nobody wants to touch it.
`expected_output.txt` is what it prints.

## Your task
1. Run it and confirm the output matches `expected_output.txt`.
2. Paste it and ask for a refactor: functions, no globals, no repeated blocks, constants named,
   a `main()` guard, **identical output**.
3. Run the refactored version and `diff` the output against `expected_output.txt`.
4. If anything differs, do not fix it yourself. Paste the diff back and ask the AI to find out why.

## How to check
`python spaghetti_refactored.py > out.txt && diff out.txt expected_output.txt` prints nothing.

## Try this
- Ask the AI: "What did you change that *could* have altered the output, and how do you know it didn't?"
  A good answer names specific risks (float summation order, rounding in prints, loop bounds) rather
  than saying "I kept the logic the same".
- Ask for a one-paragraph description of what the script does, for a README. Is it right?

## Reflect
Refactoring is the task where the AI is most likely to quietly "improve" something. Which of its
changes were improvements, and which were just differences?
