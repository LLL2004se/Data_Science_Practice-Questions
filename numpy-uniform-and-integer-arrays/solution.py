import numpy as np


def uniform_array(
    rng: np.random.Generator, low: float, high: float, shape: tuple
) -> np.ndarray:
    return rng.uniform(low, high, size=shape)


def random_integers(
    rng: np.random.Generator, low: int, high: int, shape: tuple
) -> np.ndarray:
    return rng.integers(low, high, size=shape)


def roll_dice(
    rng: np.random.Generator, n_dice: int, sides: int
) -> np.ndarray:
    return rng.integers(1, sides + 1, size=n_dice)
