import numpy as np


def rank(A):
    """
    Returns the rank of A using row reduction.
    """
    A = A.astype(float).copy()

    m, n = A.shape
    pivot_row = 0
    pivot_col = 0
    pivots = 0

    while pivot_row < m and pivot_col < n:

        # Find the row with the largest pivot
        max_row = pivot_row + np.argmax(
            np.abs(A[pivot_row:, pivot_col])
        )

        # Swap rows
        A[[pivot_row, max_row]] = A[[max_row, pivot_row]]

        # Skip column if pivot is approximately zero
        if abs(A[pivot_row, pivot_col]) < 1e-10:
            pivot_col += 1
            continue

        # Make pivot equal to 1
        A[pivot_row] = A[pivot_row] / A[pivot_row, pivot_col]

        # Eliminate other rows
        for i in range(m):
            if i != pivot_row:
                factor = A[i, pivot_col]
                A[i] -= factor * A[pivot_row]

        pivots += 1
        pivot_row += 1
        pivot_col += 1

    return pivots


def nullity(A):
    """
    Returns the nullity using the Rank-Nullity Theorem.
    """
    return A.shape[1] - rank(A)
