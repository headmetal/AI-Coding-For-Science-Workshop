"""Score an mld.py against six known profiles. Usage: python check_mld.py"""
import importlib
import os
import sys

import numpy as np

from profiles import make_profiles

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)   # so the checker finds your file when run from anywhere

try:
    mld_module = importlib.import_module("mld")
    func = getattr(mld_module, "mixed_layer_depth")
except Exception as exc:  # noqa: BLE001 - we want to report any import problem
    print(f"Could not import mixed_layer_depth from mld.py: {exc}")
    sys.exit(1)

score = 0
for name, depth, temp, expected in make_profiles():
    try:
        got = func(depth, temp)
        if np.isnan(expected):
            ok = got is None or (isinstance(got, float) and np.isnan(got)) or np.isnan(float(got))
        else:
            ok = abs(float(got) - expected) < 1.0
    except Exception as exc:  # noqa: BLE001
        got, ok = f"raised {type(exc).__name__}: {exc}", False
    score += ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:20s} expected {expected!s:>6}  got {got}")
print(f"\nScore: {score}/6")
