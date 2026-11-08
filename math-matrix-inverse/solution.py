import numpy as np


def determinant(a: np.ndarray) -> float:
    """
    Returns the determinant of a square matrix.
    """
    return float(np.linalg.det(a))


def is_invertible(a: np.ndarray) -> bool:
    """
    Checks whether a square matrix is invertible.
    """
    det = determinant(a)
    return not np.isclose(det, 0.0)


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Returns the inverse of a matrix.
    Raises LinAlgError if the matrix is not invertible.
    """
    if not is_invertible(a):
        raise np.linalg.LinAlgError("Matrix is not invertible")

    return np.linalg.inv(a)
