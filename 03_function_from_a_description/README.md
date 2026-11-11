# 03 · A function from a plain-language description

**Time:** 15–20 min · **Difficulty:** core · **Shows:** how much the quality of the ask decides the quality of the code

## The situation
You need a function that computes the ocean mixed-layer depth (MLD) from a temperature profile.
`profiles.py` generates test profiles. `check_mld.py` will test whatever you produce.

## Your task
Do this **twice**, in two separate fresh conversations.

**Round 1, the vague ask.** Paste exactly this and nothing else:
> Write a Python function that calculates mixed layer depth from a temperature profile.

Save the result as `mld.py`, with the function named `mixed_layer_depth`. Run `python check_mld.py`.

**Round 2, the specific ask.** Paste this:
> Write a Python function `mixed_layer_depth(depth, temp, threshold=0.2, ref_depth=10.0)`.
> `depth` is a 1-D numpy array of depths in metres, positive downwards, increasing, not necessarily
> starting at zero. `temp` is the matching 1-D array of temperatures in degC and may contain NaN near
> the surface. Find the reference temperature by linear interpolation at `ref_depth`. The MLD is the
> shallowest depth below `ref_depth` where the temperature differs from the reference by more than
> `threshold`, found by linear interpolation between the bracketing levels. If the threshold is never
> reached return NaN. If there is no valid temperature at or above `ref_depth`, raise a ValueError.
> Include a NumPy-style docstring and no other dependencies than numpy.

Save as `mld.py` again and re-run the check.

## How to check
`python check_mld.py` runs six profiles and prints PASS or FAIL for each, then a score out of 6.
Round 1 typically scores 2 or 3. Round 2 should score 6. If it doesn't, paste the failures back to the
AI and ask it to fix them, which is the normal loop.

## Reflect
Count the words in the two prompts. The second is about four times longer and took you maybe two
minutes to write. How long would it have taken you to discover each of those requirements by
debugging? This is slide 15 from Part 1, lived.
