"""Compare catalogue.csv to the truth. Usage: python check_catalogue.py"""
import sys

import pandas as pd

try:
    got = pd.read_csv("catalogue.csv")
    truth = pd.read_csv("_truth.csv")
except Exception as exc:  # noqa: BLE001
    print(f"Could not read catalogue.csv or _truth.csv: {exc}")
    sys.exit(1)

cols = ["model", "experiment", "variable", "start_year", "end_year", "frequency"]
missing = [c for c in cols + ["original_name"] if c not in got.columns]
if missing:
    print(f"catalogue.csv is missing columns: {missing}")
    sys.exit(1)

got = got.set_index("original_name"); truth = truth.set_index("original_name")
score = 0
for name, row in truth.iterrows():
    if name not in got.index:
        print(f"MISSING  {name}"); continue
    g = got.loc[name]
    diffs = [f"{c}: got {g[c]!r} want {row[c]!r}" for c in cols if str(g[c]).strip().lower() != str(row[c]).strip().lower()]
    if diffs:
        print(f"WRONG    {name}: " + "; ".join(diffs))
    else:
        score += 1
print(f"\nScore: {score}/{len(truth)} filenames fully correct")
