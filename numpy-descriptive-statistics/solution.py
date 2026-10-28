import numpy as np


def percentiles(a: np.ndarray, qs) -> np.ndarray:
    """The percentiles `qs` (each 0..100) of `a`, with linear interpolation."""
    a_sorted = np.sort(a)
    qs = np.asarray(qs, dtype=float)

    positions = (qs / 100.0) * (len(a_sorted) - 1)
    lower = np.floor(positions).astype(int)
    upper = np.ceil(positions).astype(int)
    weight = positions - lower

    return a_sorted[lower] * (1 - weight) + a_sorted[upper] * weight


def iqr(a: np.ndarray) -> float:
    """Interquartile range: 75th percentile minus 25th percentile."""
    q1, q3 = percentiles(a, [25, 75])
    return float(q3 - q1)


def zscores(a: np.ndarray) -> np.ndarray:
    """Standardise using population standard deviation; return zeros if std is 0."""
    mean = np.mean(a)
    std = np.std(a, ddof=0)

    if std == 0:
        return np.zeros_like(a, dtype=float)

    return (a - mean) / std


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    """Pearson correlation without np.corrcoef."""
    x_centered = x - np.mean(x)
    y_centered = y - np.mean(y)

    numerator = np.sum(x_centered * y_centered)
    denominator = np.sqrt(
        np.sum(x_centered ** 2) * np.sum(y_centered ** 2)
    )

    if denominator == 0:
        return float("nan")

    return float(numerator / denominator)


def covariance_matrix(x: np.ndarray) -> np.ndarray:
    """Sample covariance matrix of the columns of a 2D array."""
    n = x.shape[0]

    if n < 2:
        raise ValueError("At least two rows are required")

    centered = x - np.mean(x, axis=0, keepdims=True)
    return (centered.T @ centered) / (n - 1)
