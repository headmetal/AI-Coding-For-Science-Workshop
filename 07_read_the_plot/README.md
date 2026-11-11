# 07 · Read the plot

**Time:** 10 min · **Difficulty:** core · **Shows:** multimodal input, which most people have never tried

## The situation
Two images. `station_timeseries.png` is a daily temperature record from a coastal station,
2010 to 2019. `equation.png` is a formula from a whiteboard photo.

This challenge needs an AI tool that accepts images (ChatGPT, Claude, Gemini and most IDE assistants
do; many local models do not). If yours does not, pair up with someone whose tool does.

## Your task
**Image 1.** Upload `station_timeseries.png` and ask:
1. "Describe what this plot shows."
2. "Is there anything odd about this record? Be specific about when."
3. "What are plausible causes, and how would I test each one?"

**Image 2.** Upload `equation.png` and ask it to write a Python function that implements it,
with the inputs named and their units stated. Then ask what assumptions the formula makes.

## How to check
Image 1 has **two** artefacts planted in it. One is a sudden jump of a couple of degrees that persists;
the other is a short run of impossible values. A good answer finds both, dates them to within a month,
and offers instrument relocation or recalibration as the likely cause of the jump without claiming to
know. Watch for over-confidence: "this is clearly climate change" is the wrong answer.

Image 2 is the geostrophic velocity relation. A good answer names the Coriolis parameter, says the
gradient is of sea-surface height, flags that it breaks down near the equator where f goes to zero,
and gets the sign convention right or says it is a convention.

## Reflect
How much did the AI see that you did not at first glance, and the reverse? Which one of you was better
at saying "I am not sure"?
