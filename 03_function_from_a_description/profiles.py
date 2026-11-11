"""Six test temperature profiles with known mixed-layer depths (0.2 degC threshold, 10 m reference)."""
import numpy as np


def make_profiles():
    """Return a list of (name, depth, temp, expected_mld) tuples."""
    cases = []

    # 1. Textbook: uniform to 50 m then a sharp thermocline. MLD = 50 + 0.2 / 0.1 = 52 m.
    depth = np.arange(0.0, 200.0, 5.0)
    temp = np.where(depth <= 50.0, 20.0, 20.0 - 0.1 * (depth - 50.0))
    cases.append(("sharp thermocline", depth, temp, 52.0))

    # 2. Gradual: linear decrease of 0.01 degC/m from the surface. Ref at 10 m = 19.9; threshold at 30 m.
    temp = 20.0 - 0.01 * depth
    cases.append(("gradual gradient", depth, temp, 30.0))

    # 3. Surface NaN (first two levels missing), same structure as case 1.
    temp = np.where(depth <= 50.0, 20.0, 20.0 - 0.1 * (depth - 50.0))
    temp[:2] = np.nan
    cases.append(("surface NaN", depth, temp, 52.0))

    # 4. Profile does not start at zero, levels at 3, 8, 13... Ref must be interpolated at 10 m.
    depth2 = np.arange(3.0, 200.0, 5.0)
    temp = np.where(depth2 <= 50.0, 20.0, 20.0 - 0.1 * (depth2 - 50.0))
    cases.append(("offset levels", depth2, temp, 52.0))

    # 5. Threshold never reached: fully mixed to the bottom. Expect NaN.
    temp = np.full_like(depth, 20.0) + 0.001 * depth  # 0.2 degC over 200 m is never exceeded
    cases.append(("never reached", depth, temp, np.nan))

    # 6. Warm anomaly ABOVE reference must not count: warmer by 0.5 at 5 m, then uniform to 80 m. MLD = 82.
    temp = np.where(depth <= 80.0, 20.0, 20.0 - 0.1 * (depth - 80.0))
    temp[1] = 20.5
    cases.append(("surface warm spike", depth, temp, 82.0))

    return cases
