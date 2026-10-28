import numpy as np


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Return the element-wise product of a and b.
    """
    return a * b


def increment_in_place(arr: np.ndarray, amount: float) -> None:
    """
    Add amount to every element in place.
    """
    arr += amount


def square_each(arr: np.ndarray) -> np.ndarray:
    """
    Return a new array containing squared elements.
    """
    return arr ** 2


def sqrt_all(arr: np.ndarray) -> np.ndarray:
    """
    Return the element-wise square root.
    """
    return np.sqrt(arr)


def exponentiate(arr: np.ndarray) -> np.ndarray:
    """
    Return e raised to the power of each element.
    """
    return np.exp(arr)


def natural_log(arr: np.ndarray) -> np.ndarray:
    """
    Return the natural logarithm of each element.
    """
    return np.log(arr)


def absolute_values(arr: np.ndarray) -> np.ndarray:
    """
    Return the absolute value of each element.
    """
    return np.abs(arr)
