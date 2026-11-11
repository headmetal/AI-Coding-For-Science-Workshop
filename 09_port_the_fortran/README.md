# 09 · Port the Fortran

**Time:** 20 min · **Difficulty:** stretch · **Shows:** translation is where confident-but-wrong hits hardest

## The situation
`vint.f90` is a Fortran subroutine from an ocean model that vertically integrates a tracer over the
water column, using layer thicknesses and a partial bottom cell. You need it in Python, vectorised
with numpy, for an analysis script.

## Your task
1. Paste `vint.f90` and ask for a numpy port with the signature
   `vertical_integral(tracer, dz, kmt, frac_bottom)` where arrays are indexed `[k, j, i]`
   (Python order) and `kmt` holds the number of wet levels per column.
2. Save it as `vint.py` and run `python check_port.py`.
3. If a case fails, paste the failure back and ask for a fix. Count the rounds.

## How to check
`check_port.py` runs four cases and prints PASS or FAIL for each. The cases are designed to catch the
classic porting errors: 1-based vs 0-based indexing, inclusive loop bounds, column-major vs row-major
array order, and the partial-cell fraction being applied to the wrong level.

A first-attempt port very often passes the simple case and fails at least one of the others while
looking completely plausible. That is the lesson.

## Try this
- Ask the AI, before it writes any code, to list the things that commonly go wrong when porting
  Fortran to Python. Then ask it to check its own port against that list. Does the second pass catch
  anything the first missed?

## Reflect
Would you have caught the indexing error by reading the code? Be honest. What caught it here was a
test with a known answer. Where does that known answer come from in your real work?
