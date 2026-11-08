import numpy as np


def qr_decompose(A):
    """
    Decomposes A into Q and R using Gram-Schmidt.
    A = Q @ R
    """
    A = A.astype(float).copy()

    m, n = A.shape

    Q = np.zeros((m, n), dtype=float)
    R = np.zeros((n, n), dtype=float)

    for j in range(n):
        v = A[:, j].copy()

        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]

        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R
