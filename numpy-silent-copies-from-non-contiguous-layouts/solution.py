import numpy as np


def reshape_copies(arr: np.ndarray, new_shape: tuple) -> bool:
    """
    Return True if reshape creates a copy, False if it creates a view.
    """
    reshaped = arr.reshape(new_shape)
    return not np.shares_memory(reshaped, arr)


def ravel_copies(arr: np.ndarray) -> bool:
    """
    Return True if ravel creates a copy, False if it creates a view.
    """
    flattened = arr.ravel()
    return not np.shares_memory(flattened, arr)


def ensure_contiguous(arr: np.ndarray) -> np.ndarray:
    """
    Return a C-contiguous array without modifying the original.
    """
    return np.ascontiguousarray(arr)


def reshape_write_propagates(
    arr: np.ndarray, new_shape: tuple, value: int
) -> bool:
    """
    Check whether writes to a reshaped array affect the original.
    """
    result = arr.reshape(new_shape)
    result[:] = value

    return bool(np.all(arr == value))
