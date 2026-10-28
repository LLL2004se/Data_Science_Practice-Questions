import numpy as np


def join_along_existing_axis(arrays: list, axis: int) -> np.ndarray:
    """
    Join arrays along the given existing axis.
    """
    return np.concatenate(arrays, axis=axis)


def stack_as_new_axis(arrays: list) -> np.ndarray:
    """
    Combine arrays with one new leading axis.
    """
    return np.stack(arrays, axis=0)


def side_by_side(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Join 2D arrays side by side.
    """
    return np.hstack((a, b))


def stacked_vertically(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Join 2D arrays vertically.
    """
    return np.vstack((a, b))


def split_into_n_parts(arr: np.ndarray, n: int, axis: int) -> list:
    """
    Split an array into n equal parts along an axis.
    """
    return list(np.split(arr, n, axis=axis))


def split_columns(arr: np.ndarray, n: int) -> list:
    """
    Split a 2D array into n equal column-groups.
    """
    return list(np.hsplit(arr, n))


def split_result_shares_memory(arr: np.ndarray, n: int, axis: int) -> bool:
    """
    Check whether the first split result shares memory with arr.
    """
    parts = np.split(arr, n, axis=axis)
    return bool(np.shares_memory(parts[0], arr))
