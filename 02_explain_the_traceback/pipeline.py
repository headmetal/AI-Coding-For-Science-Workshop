"""Regional-mean pipeline. Fails with the traceback in traceback.txt."""
import numpy as np

REGIONS = {
    "Southern Ocean": (-90, -50),
    "Mid-lat South": (-50, -20),
    "Tropics": (-20, 20),
    "North": (20, 90),
}


def load_field():
    """Synthetic 12 x 90 x 180 (time, lat, lon) field in degC."""
    rng = np.random.default_rng(1)
    lat = np.linspace(-89, 89, 90)
    lon = np.linspace(1, 359, 180)
    base = 28.0 * np.cos(np.deg2rad(lat))[None, :, None]
    field = base + rng.normal(0, 0.5, (12, 90, 180))
    return field, lat, lon


def region_mask(lat, lon, bounds):
    lo, hi = bounds
    mask = (lat >= lo) & (lat < hi)
    return np.broadcast_to(mask[:, None], (len(lat), len(lon)))


def weights_for(lat, lon):
    w = np.cos(np.deg2rad(lat))
    return np.tile(w, (len(lon), 1))


def masked_mean(field, mask, weights):
    masked = np.where(mask, field, np.nan)
    wsum = np.nansum(weights * ~np.isnan(masked), axis=(1, 2))
    return np.nansum(masked * weights, axis=(1, 2)) / wsum


def regional_means(field, lat, lon):
    out = {}
    weights = weights_for(lat, lon)
    for name, bounds in REGIONS.items():
        mask = region_mask(lat, lon, bounds)
        out[name] = masked_mean(field, mask, weights)
    return out


def main():
    field, lat, lon = load_field()
    means = regional_means(field, lat, lon)
    assert all(np.isfinite(v).all() for v in means.values())
    print(f"Regional mean computed for {len(means)} regions: OK")


if __name__ == "__main__":
    main()
