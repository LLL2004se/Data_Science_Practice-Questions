import numpy as np


def svd(a: np.ndarray):
    """
    Computes the reduced SVD of any matrix.
    """
    u, singular_values, vt = np.linalg.svd(a, full_matrices=False)

    return u, singular_values, vt


def reconstruct_from_svd(u: np.ndarray, singular_values: np.ndarray, vt: np.ndarray) -> np.ndarray:
    """
    Reconstructs the original matrix using SVD.
    """
    return u @ np.diag(singular_values) @ vt


def low_rank_approximation(a: np.ndarray, k: int) -> np.ndarray:
    """
    Keeps only the k largest singular values and reconstructs
    the matrix using the reduced SVD.
    """
    u, singular_values, vt = svd(a)

    u_k = u[:, :k]
    s_k = singular_values[:k]
    vt_k = vt[:k, :]

    return reconstruct_from_svd(u_k, s_k, vt_k)
