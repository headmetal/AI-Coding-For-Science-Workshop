"""Check a Python port of vint.f90. Usage: python check_port.py (expects vint.py in this folder)."""
import importlib
import sys

import numpy as np

try:
    func = getattr(importlib.import_module("vint"), "vertical_integral")
except Exception as exc:  # noqa: BLE001
    print(f"Could not import vertical_integral from vint.py: {exc}")
    sys.exit(1)


def reference(tracer, dz, kmt, frac):
    """Straightforward loop translation used as the truth."""
    nk, nj, ni = tracer.shape
    out = np.zeros((nj, ni))
    for j in range(nj):
        for i in range(ni):
            kb = kmt[j, i]
            if kb == 0:
                continue
            total = 0.0
            for k in range(kb - 1):
                total += tracer[k, j, i] * dz[k]
            total += tracer[kb - 1, j, i] * dz[kb - 1] * frac[j, i]
            out[j, i] = total
    return out


rng = np.random.default_rng(7)
dz = np.array([5.0, 10.0, 20.0, 40.0, 80.0])
cases = []

# 1. One column, all five levels wet, full bottom cell: integral = sum(tracer*dz).
t = np.ones((5, 1, 1)); cases.append(("full column, uniform tracer", t, dz, np.array([[5]]), np.array([[1.0]])))

# 2. Mixed depths: kmt 1..5 across a row, random tracer, full bottom cells.
t = rng.normal(size=(5, 1, 5)); cases.append(("varying kmt", t, dz, np.arange(1, 6)[None, :], np.ones((1, 5))))

# 3. Partial bottom cells with distinct fractions, kmt = 3 everywhere: catches frac on the wrong level.
t = rng.normal(size=(5, 2, 3)); cases.append(("partial bottom cells", t, dz, np.full((2, 3), 3), rng.uniform(0.1, 0.9, (2, 3))))

# 4. Land columns (kmt = 0) mixed in, non-square grid: catches shape-order errors and land handling.
t = rng.normal(size=(5, 3, 4)); kmt = rng.integers(0, 6, (3, 4)); kmt[0, 0] = 0
cases.append(("land and non-square grid", t, dz, kmt, rng.uniform(0.2, 1.0, (3, 4))))

score = 0
for name, t, d, k, f in cases:
    want = reference(t, d, k, f)
    try:
        got = np.asarray(func(t, d, k, f), dtype=float)
        ok = got.shape == want.shape and np.allclose(got, want, atol=1e-9)
        detail = "" if ok else f"(max abs diff {np.abs(got - want).max() if got.shape == want.shape else 'shape ' + str(got.shape)})"
    except Exception as exc:  # noqa: BLE001
        ok, detail = False, f"(raised {type(exc).__name__}: {exc})"
    score += ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:28s} {detail}")
print(f"\nScore: {score}/4")
