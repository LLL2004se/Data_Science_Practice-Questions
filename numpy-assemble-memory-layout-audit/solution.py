import time
import numpy as np


def audit_array(arr: np.ndarray, new_shape: tuple) -> dict:
    # 1. Compute expected C-order strides from shape and itemsize
    expected_strides = []
    stride = arr.itemsize

    for dim in reversed(arr.shape):
        expected_strides.append(stride)
        stride *= dim

    expected_c_strides = tuple(reversed(expected_strides))

    # 2. Check whether reshape creates a copy
    reshaped = arr.reshape(new_shape)
    reshape_copies = not np.shares_memory(reshaped, arr)

    # 3. Ensure a C-contiguous version
    contiguous_version = np.ascontiguousarray(arr)
    conversion_copied = not np.shares_memory(contiguous_version, arr)

    # 4. Sum using nested Python loops
    def loop_sum():
        total = 0
        for row in arr:
            for value in row:
                total += value
        return total

    # 5. Measure best execution time over three repeats
    def best_time(func):
        best = float("inf")

        for _ in range(3):
            start = time.perf_counter()
            func()
            elapsed = time.perf_counter() - start
            best = min(best, elapsed)

        return max(float(best), float(np.finfo(float).tiny))

    loop_total = loop_sum()
    numpy_total = arr.sum()

    loop_time = best_time(loop_sum)
    numpy_time = best_time(arr.sum)

    speedup = loop_time / numpy_time

    return {
        "strides": arr.strides,
        "expected_c_strides": expected_c_strides,
        "nbytes": arr.nbytes,
        "c_contiguous": bool(arr.flags["C_CONTIGUOUS"]),
        "reshape_copies": bool(reshape_copies),
        "contiguous_version": contiguous_version,
        "conversion_copied": bool(conversion_copied),
        "sum_matches": bool(np.isclose(loop_total, numpy_total)),
        "speedup": float(speedup),
    }
