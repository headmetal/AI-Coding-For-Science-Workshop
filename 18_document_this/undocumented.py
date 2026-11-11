import numpy as np


def f1(a, b=0.0):
    w = np.cos(np.deg2rad(b))
    out = (a - 273.15) * 1.8 + 32.0
    return out * w / w if np.ndim(a) else float(out)


def f2(x, n=3):
    x = np.asarray(x)
    if x.size == 0:
        return x
    for i in range(1, len(x)):
        x[i] = x[i - 1] + (x[i] - x[i - 1]) / n
    return x


def f3(lat, lon, lat0, lon0, r=6371.0):
    p1, p2 = np.deg2rad(lat), np.deg2rad(lat0)
    dl = np.deg2rad(lon0 - lon)
    a = np.sin((p2 - p1) / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    d = 2 * r * np.arcsin(np.sqrt(a))
    return np.nanmin(d), int(np.nanargmin(d)) if np.ndim(d) else 0
