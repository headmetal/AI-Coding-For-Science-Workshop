"""Monthly anomalies plus 3x3 spatial smoothing, written with plain Python loops.

Prints the elapsed time and a checksum. Any faster version must print the same checksum.
"""
import time

import numpy as np

rng = np.random.default_rng(42)
n_time, n_lat, n_lon = 240, 180, 360
lat = np.linspace(-89.25, 89.25, n_lat)
field = (25.0 * np.cos(np.deg2rad(lat))[None, :, None]
         + 3.0 * np.cos(2 * np.pi * (np.arange(n_time) % 12) / 12.0)[:, None, None]
         + rng.normal(0.0, 0.5, (n_time, n_lat, n_lon)))

t0 = time.perf_counter()

# --- monthly climatology -----------------------------------------------------
clim = np.zeros((12, n_lat, n_lon))
for m in range(12):
    for j in range(n_lat):
        for i in range(n_lon):
            total = 0.0
            count = 0
            for t in range(m, n_time, 12):
                total += field[t, j, i]
                count += 1
            clim[m, j, i] = total / count

# --- anomalies ----------------------------------------------------------------
anom = np.zeros_like(field)
for t in range(n_time):
    for j in range(n_lat):
        for i in range(n_lon):
            anom[t, j, i] = field[t, j, i] - clim[t % 12, j, i]

# --- 3x3 smoothing of the time-mean anomaly (edges: use available neighbours) ----
mean_anom = np.zeros((n_lat, n_lon))
for j in range(n_lat):
    for i in range(n_lon):
        s = 0.0
        for t in range(n_time):
            s += anom[t, j, i]
        mean_anom[j, i] = s / n_time

smooth = np.zeros((n_lat, n_lon))
for j in range(n_lat):
    for i in range(n_lon):
        total = 0.0
        count = 0
        for dj in (-1, 0, 1):
            for di in (-1, 0, 1):
                jj, ii = j + dj, i + di
                if 0 <= jj < n_lat and 0 <= ii < n_lon:
                    total += mean_anom[jj, ii]
                    count += 1
        smooth[j, i] = total / count

elapsed = time.perf_counter() - t0
checksum = float(np.sum(np.abs(smooth)) + np.sum(np.abs(anom[::7, ::5, ::3])))
print(f"Elapsed: {elapsed:.2f} s")
print(f"Checksum: {checksum:.6f}")
