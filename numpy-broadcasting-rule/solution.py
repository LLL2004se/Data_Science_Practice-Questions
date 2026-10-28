import numpy as np


def are_broadcastable(shape_a: tuple, shape_b: tuple) -> bool:
    """
    Check whether two shapes are compatible for broadcasting.
    """
    a = shape_a[::-1]
    b = shape_b[::-1]

    for i in range(max(len(a), len(b))):
        dim_a = a[i] if i < len(a) else 1
        dim_b = b[i] if i < len(b) else 1

        if dim_a != dim_b and dim_a != 1 and dim_b != 1:
            return False

    return True


def broadcast_result_shape(shape_a: tuple, shape_b: tuple) -> tuple:
    """
    Compute the resulting broadcast shape.
    """
    a = shape_a[::-1]
    b = shape_b[::-1]
    result = []

    for i in range(max(len(a), len(b))):
        dim_a = a[i] if i < len(a) else 1
        dim_b = b[i] if i < len(b) else 1
        result.append(max(dim_a, dim_b))

    return tuple(result[::-1])


def add_scalar(matrix: np.ndarray, scalar: float) -> np.ndarray:
    """
    Add a scalar to every element of the matrix.
    """
    return matrix + scalar


def add_row_vector(matrix: np.ndarray, row_vector: np.ndarray) -> np.ndarray:
    """
    Add a row vector to every row of the matrix.
    """
    return matrix + row_vector


def add_column_vector(matrix: np.ndarray, col_values: np.ndarray) -> np.ndarray:
    """
    Add each column-vector value to its corresponding row.
    """
    return matrix + col_values[:, np.newaxis]


def outer_sum(row_values: np.ndarray, col_values: np.ndarray) -> np.ndarray:
    """
    Return an (m, n) array using broadcasting.
    """
    return col_values[:, np.newaxis] + row_values[np.newaxis, :]
