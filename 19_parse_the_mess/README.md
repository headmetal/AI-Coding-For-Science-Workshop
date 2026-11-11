# 19 · Parse the mess

**Time:** 15 min · **Difficulty:** core · **Shows:** regex and parsing, a job AI does far better than most of us

## The situation
`filenames.txt` lists 60 model output files collected from four people over ten years. The naming is
inconsistent in every way naming can be inconsistent. `run.log` is a 300-line model log with errors
and warnings buried in it.

## Your task
**Part A.** Paste `filenames.txt` **and the known-values list below** and ask for a Python script that
parses every filename into a table
with columns `model, experiment, variable, start_year, end_year, frequency, original_name`, writes it
to `catalogue.csv`, and prints any filename it could not parse. Run it. Then run
`python check_catalogue.py`.

Known values to give the AI (this is the context it cannot guess):
- Models: `ACCESS-OM2-01`, `ACCESS-OM2-025`, `ACCESS-ESM1-5`, `MOM6-panan` (sometimes written lowercase without hyphens)
- Experiments: `iaf`, `ryf`, `historical`, `ssp585`, `spinup` (sometimes upper case)
- Variables: `temp`, `salt`, `mld`, `sea_ice_conc`, `u`, `v`, `surface_heat_flux`, `aice`
- Frequencies should be normalised to `monthly`, `daily` or `annual` (from `mon`, `1m`, `monthly`, `day`, `1d`, `daily`, `ann`, `yr`)
- Two-digit years: 50–99 are 1900s, 00–49 are 2000s. Some names use `YYYYMM` ranges.

**Part B.** Paste `run.log` and ask: "Summarise what went wrong in this run, in order, with line
numbers." Then ask for a script that extracts every WARNING and ERROR with its timestamp into a table.

## How to check
`check_catalogue.py` compares your catalogue with the truth and reports mismatches. A first attempt
typically handles 50 of 60 files; the remaining ten are the ones with two-digit years, swapped
field order, or a variable name containing an underscore. Iterate.

For Part B, the log contains one fatal error, two warnings that caused it, and six warnings that are
noise. A good summary separates the chain of cause from the noise.

## Reflect
How long would writing that regex have taken you by hand? Did you read the regex it produced, or
just check the output? Which is the right thing to do here, and when would the answer be different?
