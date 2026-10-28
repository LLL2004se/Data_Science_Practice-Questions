import math


def dot_loop(a: list, b: list) -> float:
    """
    Calculate the dot product using a for loop.
    """
    total = 0.0

    for i in range(len(a)):
        total += a[i] * b[i]

    return total


def loop_time_model(n: int, per_iteration_cost: float) -> float:
    """
    Model the execution time of a Python loop.
    """
    if n <= 0:
        return 0.0

    return n * per_iteration_cost


def vectorized_time_model(
    n: int, call_overhead: float, per_element_cost: float
) -> float:
    """
    Model the execution time of a vectorized operation.
    """
    if n <= 0:
        return call_overhead

    return call_overhead + n * per_element_cost


def break_even_n(
    per_iteration_cost: float,
    call_overhead: float,
    per_element_cost: float
):
    """
    Find the smallest n where vectorization is no slower than a loop.
    """
    if per_element_cost >= per_iteration_cost:
        return None

    n = math.ceil(
        call_overhead / (per_iteration_cost - per_element_cost)
    )

    return max(1, n)


def list_of_ints_bytes(n: int) -> int:
    """
    Estimate memory used by a list of distinct small integers.
    """
    if n <= 0:
        return 0

    return n * 36


def typed_array_bytes(n: int, itemsize: int) -> int:
    """
    Calculate memory used by a typed array.
    """
    if n <= 0:
        return 0

    return n * itemsize
