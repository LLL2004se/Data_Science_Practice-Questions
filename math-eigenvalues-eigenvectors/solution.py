import numpy as np


def eigen_decomposition(a: np.ndarray):
    """
    Computes eigenvalues and eigenvectors of a real symmetric matrix.
    """
    eigenvalues, eigenvectors = np.linalg.eigh(a)

    return eigenvalues, eigenvectors


def verify_eigenpair(a: np.ndarray, eigenvalue: float, eigenvector: np.ndarray) -> bool:
    """
    Checks whether A @ v = lambda * v.
    """
    return np.allclose(
        a @ eigenvector,
        eigenvalue * eigenvector
    )
