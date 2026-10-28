import numpy as np


def sorted_copy(a: np.ndarray) -> np.ndarray:
    """Return a sorted (ascending) copy of `a`; `a` is not changed."""
    return np.sort(a)


def sort_order(a: np.ndarray) -> np.ndarray:
    """Indices that sort `a` ascending; ties keep their original order."""
    return np.argsort(a, kind="stable")


def rank_of(a: np.ndarray) -> np.ndarray:
    """
    Return the 0-based rank of every element.
    """
    order = np.argsort(a, kind="stable")
    ranks = np.empty_like(order)
    ranks[order] = np.arange(len(a))
    return ranks


def descending_order(a: np.ndarray) -> np.ndarray:
    """Indices sorting `a` descending, preserving tie order."""
    return np.argsort(-a, kind="stable")


def sort_rows_by_column(m: np.ndarray, column: int) -> np.ndarray:
    """Sort rows by one column in ascending, stable order."""
    order = np.argsort(m[:, column], kind="stable")
    return m[order]
