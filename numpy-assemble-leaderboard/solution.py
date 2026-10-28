import numpy as np


def top_k(scores: np.ndarray, k: int) -> np.ndarray:
    """Indices of the k highest scores, highest first; ties go to lower index."""
    return np.argsort(-scores, kind="stable")[:k]


def competition_ranks(scores: np.ndarray) -> np.ndarray:
    """
    1-based competition ranks; equal scores share the best rank.
    """
    return 1 + np.sum(scores[:, np.newaxis] < scores[np.newaxis, :], axis=1)


def kth_largest(scores: np.ndarray, k: int):
    """Return the k-th largest value using a partial sort."""
    if k < 1 or k > scores.size:
        raise ValueError("k must be between 1 and the number of scores")

    return np.partition(scores, scores.size - k)[scores.size - k]


def percentile_rank(scores: np.ndarray) -> np.ndarray:
    """Fraction of scores strictly smaller than each score."""
    sorted_scores = np.sort(scores)
    counts = np.searchsorted(sorted_scores, scores, side="left")
    return counts / scores.size
