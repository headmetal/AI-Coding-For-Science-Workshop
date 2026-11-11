"""Daily SST series 1983-2020 with three planted marine heatwaves. Prints the true events and saves sst_daily.csv."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(14)
dates = pd.date_range("1983-01-01", "2020-12-31", freq="D")
doy = dates.dayofyear.to_numpy()
sst = 18 + 4 * np.cos(2 * np.pi * (doy - 40) / 365.25) + rng.normal(0, 0.7, len(dates))
sst = sst + np.convolve(rng.normal(0, 0.35, len(dates)), np.ones(3) / 3, "same")

events = [("2014-02-10", "2014-02-24"), ("2016-01-05", "2016-02-14"), ("2019-07-20", "2019-07-31")]
for start, end in events:
    m = (dates >= start) & (dates <= end)
    sst[m] += 3.0 + 0.8 * np.sin(np.linspace(0, np.pi, m.sum()))

pd.DataFrame({"date": dates, "sst": np.round(sst, 3)}).to_csv("sst_daily.csv", index=False)
print("Saved sst_daily.csv. True heatwave events (inclusive):")
for start, end in events:
    print(f"  {start} to {end}  ({(pd.Timestamp(end) - pd.Timestamp(start)).days + 1} days)")
