import math


def squares_of_evens(numbers: list) -> list:
    return [n * n for n in numbers if n % 2 == 0]


def label_parity(numbers: list) -> list:
    return ["even" if n % 2 == 0 else "odd" for n in numbers]


def flatten(nested: list) -> list:
    return [item for sublist in nested for item in sublist]


def multiplication_table(n: int) -> list:
    return [[i * j for j in range(1, n + 1)]
            for i in range(1, n + 1)] if n > 0 else []


def elementwise(func, *vectors) -> list:
    return [func(*items) for items in zip(*vectors)]


def mask_select(values: list, mask: list) -> list:
    return [value for value, flag in zip(values, mask) if flag]


def broadcast_add(values: list, other) -> list:
    if hasattr(other, "__len__"):
        return [a + b for a, b in zip(values, other)]
    return [a + other for a in values]


def normalize(values: list, eps: float) -> list:
    if not values:
        return []

    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)

    return [(x - mean) / math.sqrt(variance + eps) for x in values]
