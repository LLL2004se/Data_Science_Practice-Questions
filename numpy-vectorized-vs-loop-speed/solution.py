import time
import numpy as np


def multiply_with_loop(arr: np.ndarray, factor: float) -> np.ndarray:
    """
    Multiply every element using an explicit Python loop.
    """
    result = np.empty_like(arr, dtype=np.result_type(arr, factor))

    for i in range(arr.size):
        result.flat[i] = arr.flat[i] * factor

    return result


def multiply_vectorized(arr: np.ndarray, factor: float) -> np.ndarray:
    """
    Multiply every element using vectorization.
    """
    return arr * factor


def time_both_approaches(arr: np.ndarray, factor: float) -> dict:
    """
    Time both approaches and compare their execution times.
    """
    start = time.perf_counter()
    loop_result = multiply_with_loop(arr, factor)
    loop_time_seconds = time.perf_counter() - start

    start = time.perf_counter()
    vectorized_result = multiply_vectorized(arr, factor)
    vectorized_time_seconds = time.perf_counter() - start

    return {
        "loop_result": loop_result,
        "vectorized_result": vectorized_result,
        "loop_time_seconds": float(loop_time_seconds),
        "vectorized_time_seconds": float(vectorized_time_seconds),
        "vectorized_was_faster": bool(
            vectorized_time_seconds < loop_time_seconds
        ),
    }
