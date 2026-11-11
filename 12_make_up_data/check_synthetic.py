"""Check synthetic.csv against the challenge 12 specification. Usage: python check_synthetic.py"""
import sys

import numpy as np
import pandas as pd

try:
    df = pd.read_csv("synthetic.csv", parse_dates=["date"])
except Exception as exc:  # noqa: BLE001
    print(f"Could not read synthetic.csv with columns date,temperature: {exc}")
    sys.exit(1)

results = []
def check(name, ok, detail): results.append((name, bool(ok), detail))

# Dates
expected_dates = pd.date_range("2000-01-01", "2019-12-31", freq="D")
check("date range and daily spacing", df["date"].equals(pd.Series(expected_dates)), f"{len(df)} rows, {df['date'].min().date()} to {df['date'].max().date()}")

t = df["temperature"].to_numpy(dtype=float)
valid = ~np.isnan(t)
years = (df["date"] - df["date"].iloc[0]).dt.days.to_numpy() / 365.25

# Gaps
runs = []
in_gap = False
for i, v in enumerate(valid):
    if not v and not in_gap:
        start, in_gap = i, True
    elif v and in_gap:
        runs.append((start, i - start)); in_gap = False
if in_gap: runs.append((start, len(valid) - start))
lengths = sorted(l for _, l in runs)
check("exactly three gaps of 7, 30 and 90 days", lengths == [7, 30, 90], f"gap lengths found: {lengths}")
first_last = any(df['date'].iloc[s].year in (2000, 2019) or df['date'].iloc[s + l - 1].year in (2000, 2019) for s, l in runs)
check("no gap in first or last year", runs and not first_last, f"gap start dates: {[str(df['date'].iloc[s].date()) for s, _ in runs]}")

# Trend and seasonal cycle by least squares on valid points
doy = df["date"].dt.dayofyear.to_numpy()
X = np.column_stack([np.ones(valid.sum()), years[valid], np.cos(2 * np.pi * doy[valid] / 365.25), np.sin(2 * np.pi * doy[valid] / 365.25)])
coef, *_ = np.linalg.lstsq(X, t[valid], rcond=None)
trend = coef[1]; amp = np.hypot(coef[2], coef[3]); phase_doy = (np.degrees(np.arctan2(coef[3], coef[2])) % 360) / 360 * 365.25
check("trend 0.03 degC/yr (0.02 to 0.04)", 0.02 <= trend <= 0.04, f"fitted trend {trend:.4f} degC/yr")
check("seasonal amplitude 8 degC (7.5 to 8.5)", 7.5 <= amp <= 8.5, f"fitted amplitude {amp:.2f} degC")
check("seasonal peak on ~20 January (day 10 to 30)", 10 <= phase_doy <= 30, f"fitted peak day of year {phase_doy:.0f}")

# Noise: residual std and lag-1 autocorrelation over valid consecutive pairs
resid = np.full_like(t, np.nan); resid[valid] = t[valid] - X @ coef
check("noise std 1.5 degC (1.3 to 1.7)", 1.3 <= np.nanstd(resid) <= 1.7, f"residual std {np.nanstd(resid):.2f}")
pairs = valid[:-1] & valid[1:]
r1 = np.corrcoef(resid[:-1][pairs], resid[1:][pairs])[0, 1]
check("lag-1 autocorrelation 0.7 (0.6 to 0.8)", 0.6 <= r1 <= 0.8, f"lag-1 autocorrelation {r1:.2f}")

for name, ok, detail in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name:45s} {detail}")
print(f"\nScore: {sum(ok for _, ok, _ in results)}/{len(results)}")
