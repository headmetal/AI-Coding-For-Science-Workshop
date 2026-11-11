# 04 · Make it faster

**Time:** 15 min · **Difficulty:** core · **Shows:** optimisation, and the value of asking "why"

## The situation
`slow_anomaly.py` computes monthly anomalies and a 3x3 spatial smoothing for a 10-year, 1.5-degree
global field using plain Python loops. It takes roughly 10 to 40 seconds depending on your machine, and prints a checksum.

## Your task
1. Run it once and note the time and the checksum.
2. Paste the script and ask the AI to make it as fast as possible **without changing the result**.
3. Run the new version. Compare the time and the checksum. The checksum must match to 6 decimal places.
4. Ask the AI to **explain why** its version is faster, in terms a non-programmer could follow.
5. Ask whether it could go faster still, and what the trade-offs would be. Notice whether it reaches
   for extra dependencies (numba, dask, xarray) and whether it says so.

## How to check
Same checksum, printed time at least 20x smaller. A good vectorised version runs in well under a second.

## Try this
- Ask it to add a timing comparison that runs both versions and asserts they agree.
- Deliberately ask for the *wrong* thing: "make this faster by using fewer time steps". Does it push
  back, or silently change the answer?

## Reflect
The speed-up is impressive but not the point. The point is that you can now ask "why" for free, and the
explanation is the thing you keep.
