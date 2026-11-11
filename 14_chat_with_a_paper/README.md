# 14 · Chat with a paper

**Time:** 15–20 min · **Difficulty:** core · **Shows:** methods to pseudocode to code, and finding what the paper left out

## The situation
`methods_section.md` is the methods section of a (fictional) paper on detecting marine heatwaves in
a model output. You want to reproduce it.

## Your task
1. Paste the methods section and ask for the algorithm as numbered pseudocode.
2. Ask: "What information would I need that this section does not give me?" Make your own list first,
   then compare.
3. Ask for a Python implementation of the detection step as a function that takes a daily SST series
   and returns the start and end dates of each event. Run it on `sst_daily.csv`, produced by
   `python make_test_series.py`, which has three large planted heatwaves on top of realistic noise.

## How to check
`python make_test_series.py` prints the three planted events. A correct implementation finds them with
the **start dates exact** and the end dates within three days (noise can extend an event's tail). It will
also find roughly 55 to 65 shorter events from natural variability. That is not a bug: a 90th-percentile
threshold means about one day in ten exceeds it, and runs of five happen. If you find far fewer than 50
events, or the planted ones are missing or split, something is wrong. Typical failures: the climatology
window applied wrongly at the ends of the year, "at least five days" implemented as "more than five",
and the gap-joining rule skipped.

The missing-information list should include at least: the percentile calculation method (how ties and
the window are handled), whether the baseline is fixed or moving, the treatment of the leap day, and
how events at the edges of the record are treated. The section is silent on all four, on purpose.

## Reflect
The AI found the gaps faster than you did, probably. But it also filled some of them silently when it
wrote the code. Which assumptions did it make without telling you? Go back and look.
