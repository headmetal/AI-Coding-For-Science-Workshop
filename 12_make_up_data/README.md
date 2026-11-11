# 12 · Make up data (on purpose)

**Time:** 15 min · **Difficulty:** core · **Shows:** synthetic data generation against a specification, and checking it

## The situation
You want to test a processing pipeline before the real data arrive. You need a fake dataset with
known, controllable properties. `check_synthetic.py` will test whatever you produce against the spec.

## Your task
Ask the AI to write `make_synthetic.py` that saves `synthetic.csv` with columns `date,temperature`
meeting this specification. Paste the spec exactly:

> Daily data from 2000-01-01 to 2019-12-31 inclusive. A seasonal cycle with amplitude 8 degC peaking
> on 20 January. A linear warming trend of 0.03 degC per year. Red noise with a lag-1 autocorrelation
> of 0.7 and a standard deviation of 1.5 degC. Exactly three gaps of missing data (empty cells), of
> lengths 7, 30 and 90 days, not overlapping, none in the first or last year. Use a fixed random seed.
> No dependencies other than numpy and pandas.

Run it, then run `python check_synthetic.py`.

## How to check
The checker reports each requirement as PASS or FAIL with the measured value. A first attempt usually
gets the trend and seasonality right and gets the autocorrelation or the gap placement wrong. Paste
the failures back and iterate.

## Try this
- Ask the AI to explain how it generated the red noise and what "lag-1 autocorrelation of 0.7" means
  physically. Then ask how it chose the gap positions. Was it random or did it pick convenient dates?
- Ask it to add an option that injects a step change on a given date. Now you have challenge 07's plot.

## Reflect
Synthetic data is only as good as the spec. What did you leave out of the spec that the AI had to
guess? Did it tell you it was guessing?
