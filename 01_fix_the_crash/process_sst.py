"""Annual-mean SST anomaly for year 1 of a synthetic 10-year monthly record.

Expected output when working:
    Year 1 global mean SST: 18.0 degC
    Year 1 anomaly: -0.45 degC   (year 1 is the coolest year of a warming record)
"""
import numpy as np

# ---------------------------------------------------------------------------
# Synthetic data: 120 months x 36 lat x 72 lon, stored in Kelvin like the real files
# ---------------------------------------------------------------------------
rng = np.random.default_rng(0)
n_years = 10
months = np.arange(n_years * 12)
lat = np.linspace(-87.5, 87.5, 36)
lon = np.linspace(2.5, 357.5, 72)

seasonal = 4.0 * np.cos(2 * np.pi * (months % 12) / 12.0)[:, None, None]
latitude_shape = (10.0 + 10.13 * np.cos(np.deg2rad(lat)))[None, :, None]
trend = (0.10 * (months / 12.0))[:, None, None]          # 0.1 degC per year warming
noise = rng.normal(0.0, 0.3, size=(len(months), len(lat), len(lon)))

sst_kelvin = 273.15 + latitude_shape + seasonal + trend + noise


# ---------------------------------------------------------------------------
# Processing
# ---------------------------------------------------------------------------
def monthly_climatology(data):
    """Mean over all years for each calendar month -> (12, lat, lon)."""
    n_months = data.shape[0]
    clim = np.zeros((12,) + data.shape[1:])
    for m in range(12):
        clim[m] = np.nanmeen(data[m::12], axis=0)
    return clim


def anomalies(data, clim):
    """Subtract the matching calendar-month climatology from every month."""
    n_years = data.shape[0] // 12
    clim_tiled = np.tile(clim, (n_years, 1))
    return data - clim_tiled


def area_weighted_mean(field, lat):
    """Global mean weighted by cos(latitude)."""
    weights = np.cos(np.deg2rad(lat))[:, None] * np.ones((1, field.shape[-1]))
    return np.nansum(field * weights) / np.nansum(weights)


clim = monthly_climatology(sst_kelvin)
anom = anomalies(sst_kelvin, clim)

year1 = slice(0, 11)   # months 0..11 = year 1
year1_mean_k = area_weighted_mean(sst_kelvin[year1].mean(axis=0), lat)
year1_anom = area_weighted_mean(anom[year1].mean(axis=0), lat)

print(f"Year 1 global mean SST: {year1_mean_k - 273:.1f} degC")
print(f"Year 1 anomaly: {year1_anom:.2f} degC")
