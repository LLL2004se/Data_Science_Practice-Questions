import numpy as np


def normalize_rows(data: np.ndarray) -> np.ndarray:
    """
    Normalize each row using broadcasting.
    """
    row_mean = data.mean(axis=1, keepdims=True)
    row_std = data.std(axis=1, keepdims=True)

    return (data - row_mean) / row_std


def pairwise_differences(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Return an (m, n) array where result[i, j] = a[j] - b[i].
    """
    return a[np.newaxis, :] - b[:, np.newaxis]


def scale_columns(matrix: np.ndarray, scale_factors: np.ndarray) -> np.ndarray:
    """
    Multiply each column by its corresponding scale factor.
    """
    return matrix * scale_factors
