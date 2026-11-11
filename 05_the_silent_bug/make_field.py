"""Build the synthetic Southern Hemisphere sea-ice concentration field used by sea_ice_extent.py.

Writes sic_synthetic.npz containing:
    sic   (12, nlat, nlon)  sea-ice concentration in PERCENT (0-100), as in the satellite products
    lat   (nlat,)           cell-centre latitudes, 1-degree grid, 89.5S to 40.5S
    lon   (nlon,)           cell-centre longitudes, 0.5 to 359.5

Run once:  python make_field.py
"""
import numpy as np

lat = np.arange(-89.5, -39.5, 1.0)
lon = np.arange(0.5, 360.0, 1.0)
months = np.arange(12)

# Ice edge latitude moves between ~-71.5 (Mar) and ~-63 (Sep), with a small zonal wave.
edge = -67.25 + 4.25 * np.cos(2 * np.pi * (months - 8) / 12.0)      # (12,)
wave = 2.0 * np.cos(np.deg2rad(3.0 * lon))                           # (nlon,)
LAT, LON = np.meshgrid(lat, lon, indexing="ij")
sic = np.zeros((12, lat.size, lon.size))
for m in months:
    sic[m] = 100.0 / (1.0 + np.exp((LAT - (edge[m] + wave[None, :])) / 1.5))
sic[:, LAT < -70.0] = 0.0                      # Antarctic continent (approximated as everything south of 70S)
sic = np.clip(sic, 0.0, 100.0)

np.savez_compressed("sic_synthetic.npz", sic=sic.astype(np.float32), lat=lat, lon=lon)
print(f"wrote sic_synthetic.npz  sic{sic.shape}  range {sic.min():.1f}-{sic.max():.1f}")
