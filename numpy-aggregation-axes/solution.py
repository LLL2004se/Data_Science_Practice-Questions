import numpy as np


def compute_summary(arr: np.ndarray) -> dict:
    """
    Compute summary statistics for a 1D array.
    """
    return {
        "sum": arr.sum(),
        "mean": arr.mean(),
        "std": arr.std(),
        "min": arr.min(),
        "max": arr.max(),
        "argmin": arr.argmin(),
        "argmax": arr.argmax(),
    }


def sum_with_loop(arr: np.ndarray) -> float:
    """
    Compute the sum using an explicit Python loop.
    """
    total = 0.0

    for value in arr:
        total += value

    return total


def sum_along_axis(arr: np.ndarray, axis: int) -> np.ndarray:
    """
    Sum the array along the specified axis.
    """
    return arr.sum(axis=axis)


def mean_keeping_dims(arr: np.ndarray, axis: int) -> np.ndarray:
    """
    Compute the mean while retaining the reduced dimension.
    """
    return arr.mean(axis=axis, keepdims=True)


def column_maxes(matrix: np.ndarray) -> np.ndarray:
    """
    Return the maximum value of each column.
    """
    return matrix.max(axis=0)


def row_argmins(matrix: np.ndarray) -> np.ndarray:
    """
    Return the column index of each row's minimum value.
    """
    return matrix.argmin(axis=1)
