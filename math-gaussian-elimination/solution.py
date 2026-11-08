import numpy as np


def gaussian_eliminate(A, b):
    """
    Converts A into upper-triangular form using Gaussian elimination.
    """
    A = A.astype(float).copy()
    b = b.astype(float).copy()

    n = len(b)

    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]

            A[j, :] = A[j, :] - factor * A[i, :]
            b[j] = b[j] - factor * b[i]

    return A, b


def back_substitute(U, c):
    """
    Solves Ux = c using back substitution.
    """
    n = len(c)
    x = np.zeros(n, dtype=float)

    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x
