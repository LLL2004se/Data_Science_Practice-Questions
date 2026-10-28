import numpy as np


def process_feature_batch(
    data: np.ndarray, feature_scales: np.ndarray, bias_per_sample: np.ndarray
) -> dict:
    """
    Scale features, add per-sample bias, and test broadcasting.
    """
    # Step 1: Scale each column
    scaled = data * feature_scales

    # Step 2: Add bias to each row
    biased = scaled + bias_per_sample[:, np.newaxis]

    # Step 3: Attempt direct addition without reshaping
    try:
        direct_add_result = biased + feature_scales
        direct_add_success = True
    except ValueError:
        direct_add_result = None
        direct_add_success = False

    # Step 4: Predict the broadcast shape directly
    shape_a = biased.shape
    shape_b = (bias_per_sample.shape[0], 1)

    aligned_a = shape_a[::-1]
    aligned_b = shape_b[::-1]
    result_shape = []

    for i in range(max(len(aligned_a), len(aligned_b))):
        dim_a = aligned_a[i] if i < len(aligned_a) else 1
        dim_b = aligned_b[i] if i < len(aligned_b) else 1
        result_shape.append(max(dim_a, dim_b))

    predicted_broadcast_shape = tuple(result_shape[::-1])

    return {
        "scaled": scaled,
        "biased": biased,
        "direct_add_success": direct_add_success,
        "direct_add_result": direct_add_result,
        "predicted_broadcast_shape": predicted_broadcast_shape,
    }
