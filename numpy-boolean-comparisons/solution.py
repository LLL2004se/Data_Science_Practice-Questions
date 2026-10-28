import numpy as np


def in_range_mask(arr: np.ndarray, low: float, high: float) -> np.ndarray:
    """
    Return True where values are strictly between low and high.
    """
    return (arr > low) & (arr < high)


def outside_range_mask(arr: np.ndarray, low: float, high: float) -> np.ndarray:
    """
    Return True where values are below low or above high.
    """
    return (arr < low) | (arr > high)


def not_matching(arr: np.ndarray, value: float) -> np.ndarray:
    """
    Return True where values do not equal the specified value.
    """
    return ~(arr == value)
