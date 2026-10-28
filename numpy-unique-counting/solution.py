import numpy as np


def distinct(a: np.ndarray) -> np.ndarray:
    """Sorted distinct values of `a`."""
    return np.unique(a)


def value_counts(a: np.ndarray):
    """Return sorted distinct values and their counts."""
    values, counts = np.unique(a, return_counts=True)
    return values, counts


def first_positions(a: np.ndarray) -> np.ndarray:
    """Return first occurrence indices for sorted distinct values."""
    _, indices = np.unique(a, return_index=True)
    return indices


def codes(a: np.ndarray) -> np.ndarray:
    """Return the sorted-unique index for each element."""
    _, inverse = np.unique(a, return_inverse=True)
    return inverse


def mode(a: np.ndarray):
    """Return the most frequent value; smallest value wins ties."""
    values, counts = np.unique(a, return_counts=True)
    return values[np.argmax(counts)]


def unique_in_order(a: np.ndarray) -> np.ndarray:
    """Return distinct values in first-appearance order."""
    indices = np.unique(a, return_index=True)[1]
    return a[np.sort(indices)]
