import time
import numpy as np


def loop_sum_of_squares(values: list) -> int:
    total = 0

    for value in values:
        total += value * value

    return total


def vectorized_sum_of_squares(arr: np.ndarray) -> int:
    values = arr.astype(np.int64, copy=False)
    return int(np.dot(values, values))


def best_time(func, args: tuple, repeats: int) -> float:
    best = float("inf")

    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        elapsed = time.perf_counter() - start
        best = min(best, elapsed)

    return max(float(best), float(np.finfo(float).tiny))


def benchmark_sum_of_squares(n: int, repeats: int = 3) -> dict:
    values = list(range(n))
    arr = np.arange(n, dtype=np.int64)

    loop_result = loop_sum_of_squares(values)
    vec_result = vectorized_sum_of_squares(arr)

    loop_time = best_time(loop_sum_of_squares, (values,), repeats)
    vec_time = best_time(vectorized_sum_of_squares, (arr,), repeats)

    speedup = loop_time / vec_time if vec_time > 0 else 0.0

    return {
        "loop_time": float(loop_time),
        "vec_time": float(vec_time),
        "speedup": float(speedup),
        "results_match": bool(loop_result == vec_result),
    }
