import numpy as np


def make_regression_dataset(
    seed: int,
    n_samples: int,
    n_features: int,
    noise_std: float,
    test_fraction: float,
    hidden_units: int,
) -> dict:
    rng = np.random.default_rng(seed)

    # 1. Generate input features
    X = rng.standard_normal((n_samples, n_features))

    # 2. Generate true weights
    true_w = rng.uniform(-1.0, 1.0, n_features)

    # 3. Generate noise
    noise = rng.normal(0.0, noise_std, n_samples)

    # 4. Generate train/test split mask
    split = rng.random(n_samples)

    # 5. Initialize neural network weights
    W_init = rng.normal(
        0.0,
        np.sqrt(2.0 / n_features),
        (n_features, hidden_units),
    )

    # Calculate target values
    y = X @ true_w + noise

    # Split the dataset while preserving row order
    is_test = split < test_fraction
    is_train = ~is_test

    return {
        "X_train": X[is_train],
        "y_train": y[is_train],
        "X_test": X[is_test],
        "y_test": y[is_test],
        "true_w": true_w,
        "W_init": W_init,
    }
