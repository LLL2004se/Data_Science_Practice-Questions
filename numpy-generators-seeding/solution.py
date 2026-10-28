import numpy as np


def create_rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def make_independent_rngs(seed_a: int, seed_b: int) -> tuple:
    rng_a = create_rng(seed_a)
    rng_b = create_rng(seed_b)
    return rng_a, rng_b


def draw(rng: np.random.Generator, n: int) -> np.ndarray:
    return rng.random(n)


def reproducible_draw(seed: int, n: int) -> np.ndarray:
    rng = create_rng(seed)
    return rng.random(n)


def draw_twice(seed: int, n: int) -> tuple:
    rng = create_rng(seed)
    first = rng.random(n)
    second = rng.random(n)
    return first, second


def same_seed_same_output(seed: int, n: int) -> bool:
    rng_a = create_rng(seed)
    rng_b = create_rng(seed)

    values_a = rng_a.random(n)
    values_b = rng_b.random(n)

    return bool(np.array_equal(values_a, values_b))


def skip_then_draw(
    rng: np.random.Generator, skip: int, n: int
) -> np.ndarray:
    rng.random(skip)
    return rng.random(n)
