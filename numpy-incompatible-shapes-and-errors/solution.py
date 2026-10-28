import numpy as np


def try_broadcast_add(a: np.ndarray, b: np.ndarray) -> dict:
    """
    Attempt to compute a + b and report whether it succeeded.
    """
    try:
        result = a + b
        return {
            "success": True,
            "result": result,
            "shape_a": a.shape,
            "shape_b": b.shape,
        }
    except ValueError:
        return {
            "success": False,
            "result": None,
            "shape_a": a.shape,
            "shape_b": b.shape,
        }


def find_first_incompatible_axis(shape_a: tuple, shape_b: tuple):
    """
    Find the first incompatible axis, counting from the right.
    """
    max_dims = max(len(shape_a), len(shape_b))

    for i in range(1, max_dims + 1):
        dim_a = shape_a[-i] if i <= len(shape_a) else 1
        dim_b = shape_b[-i] if i <= len(shape_b) else 1

        if dim_a != dim_b and dim_a != 1 and dim_b != 1:
            return -i

    return None
