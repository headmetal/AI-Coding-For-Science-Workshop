# 05 · The silent bug

**Time:** 15–20 min · **Difficulty:** core · **Shows:** the AI cannot tell you what you did not ask

## The situation
`sea_ice_extent.py` computes monthly Southern Hemisphere sea-ice extent from a synthetic
concentration field on a regular 1-degree grid. It runs cleanly, prints twelve sensible-looking
numbers, and is wrong. A colleague who knows the data says the September value is "way too high, several times what it should be".

## Your task
1. Run it. Look at the numbers. They look fine. That is the point.
2. Paste the script and ask the AI, nothing more: "Is this correct?" Note the answer. Do not tell it
   there is a bug, how many, or what your colleague said.
3. Now paste it again in a fresh conversation with the colleague's comment: "The September extent is
   about four times too high. Find the bug." Note the difference.
4. Fix it, re-run, and check.

## How to check
Correct September extent for this synthetic field is between 17.5 and 19.0 million km².
Correct February extent is between 2.0 and 3.5 million km². There are **two** bugs; fixing one
gets you most of the way, fixing both gets you inside the ranges.

## Try this
- Ask the AI to write a test that would have caught this. Would it have? What does the test need
  to know that the code didn't?

## Reflect
In step 2, did the AI find both bugs, find one, hedge, or say the code was fine? The answer depends
heavily on which model you used and on exactly what you typed. If it found both unprompted, try the
same question on a smaller or older model, or with the comments stripped out of the script. If it
hedged, that hedge is a signal worth learning to read. Either way: would you have trusted a "looks
fine" answer? Fluent code review is not the same as a correct one.
