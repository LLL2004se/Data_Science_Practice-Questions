import numpy as np


def replace_where(a: np.ndarray, mask: np.ndarray, value) -> np.ndarray:
    """A copy of `a` with `value` at the positions where boolean `mask` is True."""
    result = a.copy()
    result[mask] = value
    return result


def clip_to_percentiles(a: np.ndarray, low: float, high: float) -> np.ndarray:
    """
    Clip values into the [low-th percentile, high-th percentile] range.
    Returns a new array.
    """
    lower = np.percentile(a, low, method="linear")
    upper = np.percentile(a, high, method="linear")
    return np.clip(a, lower, upper)


def sign_class(a: np.ndarray) -> np.ndarray:
    """Return -1 for negative, 0 for zero, and 1 for positive values."""
    return np.select(
        [a < 0, a == 0, a > 0],
        [-1, 0, 1],
        default=0
    ).astype(int)


def bucket_label(a: np.ndarray, low: float, high: float) -> np.ndarray:
    """Label values as 'low', 'mid', or 'high'."""
    return np.select(
        [a < low, a >= high],
        ["low", "high"],
        default="mid"
    )
