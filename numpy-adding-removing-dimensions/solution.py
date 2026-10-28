import numpy as np


def to_column_vector(arr: np.ndarray) -> np.ndarray:
    """
    Return shape (n, 1), a column vector.
    """
    return arr[:, np.newaxis]


def to_row_vector(arr: np.ndarray) -> np.ndarray:
    """
    Return shape (1, n), a row vector.
    """
    return arr[np.newaxis, :]


def add_dimension_at(arr: np.ndarray, axis: int) -> np.ndarray:
    """
    Insert a new dimension of size 1 at position axis.
    """
    return np.expand_dims(arr, axis=axis)


def remove_all_singleton_dims(arr: np.ndarray) -> np.ndarray:
    """
    Remove every dimension of size 1.
    """
    return arr.squeeze()


def remove_singleton_at(arr: np.ndarray, axis: int) -> np.ndarray:
    """
    Remove the size-1 dimension at the specified axis.
    """
    return arr.squeeze(axis=axis)
