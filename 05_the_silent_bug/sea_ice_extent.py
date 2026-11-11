"""Monthly Southern Hemisphere sea-ice extent (million km^2) from a gridded concentration field."""
import numpy as np

d = np.load("sic_synthetic.npz")
sic, lat, lon = d["sic"], d["lat"], d["lon"]   # sic: (12, nlat, nlon), 1-degree grid

# ---------------------------------------------------------------------------
# Extent: total area of cells with at least 15% ice
# ---------------------------------------------------------------------------
EARTH_RADIUS_KM = 6371.0
deg = np.deg2rad(1.0)
cell_area_km2 = (EARTH_RADIUS_KM * deg) ** 2                         # area of a 1x1 degree cell

ice_mask = sic >= 0.15
extent_km2 = ice_mask.sum(axis=(1, 2)) * cell_area_km2

names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for name, value in zip(names, extent_km2 / 1e6):
    print(f"{name}: {value:5.2f} million km^2")
