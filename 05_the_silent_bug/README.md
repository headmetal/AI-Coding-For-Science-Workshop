# 05 · The silent bug

**Time:** 15–20 min · **Difficulty:** core · **Shows:** the AI cannot tell you what you did not give it

## The situation
`sea_ice_extent.py` computes monthly Southern Hemisphere sea-ice extent from a gridded concentration
field in `sic_synthetic.npz`. It runs cleanly, prints twelve sensible-looking numbers, and is wrong.
A colleague who knows the data says the September value is "way too high, several times what it
should be".

The data file was produced by `make_field.py`. You do not need to run it; the `.npz` is supplied.

## Your task
1. Run `sea_ice_extent.py`. Look at the numbers. They look fine. That is the point.
2. Paste **only** `sea_ice_extent.py` and ask the AI, nothing more: "Is this correct?" Note the answer.
   Do not mention a bug, a colleague, or the data file.
3. In a fresh conversation, paste the same script with the colleague's comment: "The September extent
   is about four times too high. Find the bug." Note what changes.
4. In a third conversation, paste the script **and** `make_field.py`, and ask "Is this correct?" again.
5. Fix it, re-run, and check.

## How to check
Correct September extent for this field is between 17.5 and 19.0 million km². Correct February
extent is between 2.0 and 3.5 million km². There are **two** bugs. One is visible in the script
alone. The other is only visible once you know something about the data. Fixing one gets you
partway; fixing both gets you inside the ranges.

## Try this
- Ask the AI to write a test that would have caught this. Would it have? What does the test need
  to know that the script doesn't?

## Reflect
In step 2 the AI had the script but not the data. The best it can honestly do with one of the bugs
is ask a question or state an assumption. Did it? Or did it pick an interpretation and move on?
In step 4 it had everything and probably found both. The difference is not cleverness; it is what
you gave it. Fluent code review is not the same as a correct one, and the AI cannot review what it
cannot see.
