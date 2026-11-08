import numpy as np


def lu_decompose(A):
    """
    Decomposes A into L and U such that A = L @ U.
    """
    U = A.astype(float).copy()
    n = U.shape[0]

    L = np.eye(n, dtype=float)

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]

            L[j, i] = factor

            U[j, :] = U[j, :] - factor * U[i, :]

    return L, U
