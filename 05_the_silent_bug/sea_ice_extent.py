"""Monthly Southern Hemisphere sea-ice extent (million km^2) from a synthetic concentration field.

Runs cleanly. Produces plausible-looking numbers. Contains two bugs.
"""
import numpy as np

# ---------------------------------------------------------------------------
# Synthetic concentration: 12 months x 1-degree grid, SH only (90S-40S)
# ---------------------------------------------------------------------------
lat = np.arange(-89.5, -39.5, 1.0)             # cell centres
lon = np.arange(0.0, 361.0, 1.0)               # cell centres, 0..360
months = np.arange(12)

# Ice edge latitude moves between ~-68.5 (Feb) and ~-60 (Sep), with a small zonal wave.
edge = -67.25 + 4.25 * np.cos(2 * np.pi * (months - 8) / 12.0)      # (12,)
wave = 2.0 * np.cos(np.deg2rad(3.0 * lon))                           # (nlon,)
LAT, LON = np.meshgrid(lat, lon, indexing="ij")
sic = np.zeros((12, lat.size, lon.size))
for m in months:
    sic[m] = 100.0 / (1.0 + np.exp((LAT - (edge[m] + wave[None, :])) / 1.5))
sic[:, LAT < -70.0] = 0.0                      # Antarctic continent (approximated as everything south of 70S)
sic = np.clip(sic, 0.0, 100.0)                 # concentration in percent, as in the satellite products

# ---------------------------------------------------------------------------
# Extent: total area of cells with concentration >= 15%
# ---------------------------------------------------------------------------
EARTH_RADIUS_KM = 6371.0
deg = np.deg2rad(1.0)
cell_area_km2 = (EARTH_RADIUS_KM * deg) ** 2                         # area of a 1x1 degree cell

ice_mask = sic >= 0.15
extent_km2 = ice_mask.sum(axis=(1, 2)) * cell_area_km2

names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for name, value in zip(names, extent_km2 / 1e6):
    print(f"{name}: {value:5.2f} million km^2")
