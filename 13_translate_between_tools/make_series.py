"""Generates monthly_series.csv (already provided; run only to regenerate)."""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(13)
rows = ["year,month,value"]
k = 0
for year in range(1980, 2020):
    for month in range(1, 13):
        value = 10 + 4 * np.cos(2 * np.pi * (month - 1) / 12) + 0.02 * k + rng.normal(0, 0.8)
        rows.append(f"{year},{month},{value:.3f}")
        k += 1
open(os.path.join(HERE, "monthly_series.csv"), "w").write("\n".join(rows) + "\n")
