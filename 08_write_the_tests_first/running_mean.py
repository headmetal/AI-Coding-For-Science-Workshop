"""A centred running mean. In use since 2016."""
import numpy as np


def running_mean(x, window):
    """Return the centred running mean of x with the given window length."""
    x = np.asarray(x, dtype=float)
    kernel = np.ones(window) / window
    return np.convolve(x, kernel, mode="same")


if __name__ == "__main__":
    series = np.sin(np.linspace(0, 6 * np.pi, 200)) + 0.1 * np.random.default_rng(0).normal(size=200)
    print(running_mean(series, 5)[:10])
