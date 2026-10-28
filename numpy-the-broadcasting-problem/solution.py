import numpy as np


def add_row_with_loop(matrix: np.ndarray, row: np.ndarray) -> np.ndarray:
    """
    Add row to every row of matrix using a Python loop.
    """
    result = matrix.copy()

    for i in range(matrix.shape[0]):
        result[i] = matrix[i] + row

    return result


def add_row_with_broadcasting(matrix: np.ndarray, row: np.ndarray) -> np.ndarray:
    """
    Add row to every row using NumPy broadcasting.
    """
    return matrix + row
