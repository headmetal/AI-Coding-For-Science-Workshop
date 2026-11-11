# 06 · Describe a dataset you have never opened

**Time:** 10–15 min · **Difficulty:** core · **Shows:** turning metadata into understanding in one prompt

## The situation
`ncdump_header.txt` is the header (`ncdump -h`) of an ocean model output file you have been handed.
You have not opened it and you do not know the model. The file itself is not provided; the header is
all you need for this challenge, which is exactly the point.

## Your task
Paste the header and ask, in one go:
1. Describe this file in plain language: what model, what variables, what grid, what period, what frequency.
2. List everything that could trip me up when I analyse it.
3. Write the xarray code to open it and extract the time-mean temperature at 100 m depth for the
   Southern Ocean (south of 50S), with the correct handling of whatever pitfalls you found.

## How to check
A good answer spots **at least five** of these: the time units and calendar, that temperature is in
Kelvin not Celsius, that the horizontal grid is curvilinear so lat/lon are 2-D auxiliary variables and
`sel(lat=...)` will not work, the depth axis is positive down and in metres at cell centres with bounds,
the missing value attribute, the cell methods (these are monthly means), the longitude range (-280 to 80,
not 0 to 360), and that the file is one of a series. Score your answer.

Then look at the code it wrote. Does it select "100 m" by nearest level or does it interpolate? Did it
say which? Did it mask the land?

## Try this
- Ask: "What would I need to know that is *not* in this header?" Good answers mention the grid cell
  areas for weighting, whether the model year corresponds to a calendar year, and what the experiment is.

## Reflect
Ten minutes of squinting at ncdump replaced by one prompt, but only if you then check the parts that
matter. Which of the pitfalls would have cost you a day if you had missed it?
