import numpy as np


def transpose_2d(arr: np.ndarray) -> np.ndarray:
    """
    Return the transpose of 2D array `arr` using .T.
    """
    return arr.T


def transpose_axes(arr: np.ndarray, axes: tuple) -> np.ndarray:
    """
    Return `arr` with its axes reordered according to `axes`.
    """
    return arr.transpose(axes)


def transpose_shares_memory(arr: np.ndarray) -> bool:
    """
    Return True if arr.T shares memory with arr, False otherwise.
    """
    return bool(np.shares_memory(arr.T, arr))
