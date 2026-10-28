import numpy as np


def summary_ignoring_nan(a: np.ndarray) -> dict:
    """
    Summary statistics over non-NaN values.
    If no known values exist, return count 0 and NaN for the rest.
    """
    count = int(np.sum(~np.isnan(a)))

    if count == 0:
        return {
            "count": 0,
            "mean": float("nan"),
            "std": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
        }

    return {
        "count": count,
        "mean": float(np.nanmean(a)),
        "std": float(np.nanstd(a, ddof=0)),
        "min": float(np.nanmin(a)),
        "max": float(np.nanmax(a)),
    }


def count_missing(m: np.ndarray, axis: int) -> np.ndarray:
    """Number of NaN entries along the specified axis."""
    return np.sum(np.isnan(m), axis=axis)


def fill_with_column_means(m: np.ndarray) -> np.ndarray:
    """
    Replace NaNs with column means; use 0.0 for entirely NaN columns.
    Do not modify the original array.
    """
    result = m.copy()
    means = np.nanmean(result, axis=0)
    means = np.where(np.isnan(means), 0.0, means)

    rows, cols = np.where(np.isnan(result))
    result[rows, cols] = means[cols]

    return result


def rows_without_nan(m: np.ndarray) -> np.ndarray:
    """Return rows containing no NaN values."""
    mask = ~np.isnan(m).any(axis=1)
    return m[mask]


def argmax_ignoring_nan(a: np.ndarray) -> int:
    """Index of the largest non-NaN value, or -1 if all values are NaN."""
    valid = ~np.isnan(a)

    if not np.any(valid):
        return -1

    return int(np.nanargmax(a))
