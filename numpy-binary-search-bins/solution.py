import numpy as np


def insertion_points(sorted_a: np.ndarray, values: np.ndarray, side: str) -> np.ndarray:
    """Where each value would be inserted into sorted_a."""
    return np.searchsorted(sorted_a, values, side=side)


def count_between(sorted_a: np.ndarray, lo, hi) -> int:
    """Count elements satisfying lo <= x <= hi using two binary searches."""
    left = np.searchsorted(sorted_a, lo, side="left")
    right = np.searchsorted(sorted_a, hi, side="right")
    return int(max(0, right - left))


def bucketize(values: np.ndarray, edges: np.ndarray) -> np.ndarray:
    """Return the number of edges <= each value."""
    return np.searchsorted(edges, values, side="right")


def nearest_value(sorted_a: np.ndarray, targets: np.ndarray) -> np.ndarray:
    """Find nearest values, choosing the smaller value on ties."""
    if sorted_a.size == 0:
        raise ValueError("sorted_a must not be empty")

    indices = np.searchsorted(sorted_a, targets, side="left")
    right = np.clip(indices, 0, len(sorted_a) - 1)
    left = np.clip(indices - 1, 0, len(sorted_a) - 1)

    left_dist = np.abs(targets - sorted_a[left])
    right_dist = np.abs(targets - sorted_a[right])

    return np.where(left_dist <= right_dist, sorted_a[left], sorted_a[right])


def is_present(sorted_a: np.ndarray, values: np.ndarray) -> np.ndarray:
    """Check whether each value exists in sorted_a."""
    indices = np.searchsorted(sorted_a, values, side="left")
    valid = indices < len(sorted_a)

    result = np.zeros(values.shape, dtype=bool)
    result[valid] = sorted_a[indices[valid]] == values[valid]

    return result
