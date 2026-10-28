import numpy as np


def analyze_dataset(data: np.ndarray, lower_bound: float, upper_bound: float) -> dict:
    """
    Analyze a 2D dataset using vectorized NumPy operations.
    """
    # 1. Absolute value followed by square root
    transformed = np.sqrt(np.abs(data))

    # 2. Find values strictly between the bounds
    valid_mask = (transformed > lower_bound) & (transformed < upper_bound)

    # 3. Count all True values
    valid_count = int(np.sum(valid_mask))

    # 4. Mean of each feature (column)
    feature_means = transformed.mean(axis=0)

    # 5. Maximum value of each sample (row)
    sample_maxes = transformed.max(axis=1)

    return {
        "transformed": transformed,
        "valid_mask": valid_mask,
        "valid_count": valid_count,
        "feature_means": feature_means,
        "sample_maxes": sample_maxes,
    }
