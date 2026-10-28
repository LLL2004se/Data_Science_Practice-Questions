import numpy as np


def running_total(a: np.ndarray) -> np.ndarray:
    """Cumulative sum of `a`."""
    return np.cumsum(a)


def cumulative_max(a: np.ndarray) -> np.ndarray:
    """Running maximum: element i is max(a[0..i])."""
    return np.maximum.accumulate(a)


def consecutive_differences(a: np.ndarray) -> np.ndarray:
    """a[i+1] - a[i] for every neighbouring pair."""
    return a[1:] - a[:-1]


def percent_change(a: np.ndarray) -> np.ndarray:
    """
    Relative change between neighbouring values.
    Returns NaN where the previous value is zero.
    """
    previous = a[:-1].astype(float)
    current = a[1:].astype(float)

    result = np.full(len(a) - 1, np.nan, dtype=float)
    np.divide(
        current - previous,
        previous,
        out=result,
        where=previous != 0
    )
    return result


def moving_average(a: np.ndarray, w: int) -> np.ndarray:
    """
    Mean of every window of w consecutive values using cumulative sums.
    """
    if w < 1 or w > len(a):
        raise ValueError("w must be between 1 and len(a)")

    cumulative = np.concatenate(([0], np.cumsum(a, dtype=float)))
    window_sums = cumulative[w:] - cumulative[:-w]
    return window_sums / w
