import numpy as np


def compute_c_strides(shape: tuple, itemsize: int) -> tuple:
    """
    Compute C-order strides without creating an array.
    """
    strides = []
    stride = itemsize

    for dim in reversed(shape):
        strides.append(stride)
        stride *= dim

    return tuple(reversed(strides))


def byte_offset(index: tuple, strides: tuple) -> int:
    """
    Calculate the byte offset for an array index.
    """
    return sum(i * s for i, s in zip(index, strides))


def slice_step_strides(arr: np.ndarray, step: int) -> tuple:
    """
    Compute strides for slicing along axis 0.
    """
    return (arr.strides[0] * step,) + arr.strides[1:]


def contiguity_flags(arr: np.ndarray) -> dict:
    """
    Return C- and Fortran-contiguity flags.
    """
    return {
        "c_contiguous": bool(arr.flags["C_CONTIGUOUS"]),
        "f_contiguous": bool(arr.flags["F_CONTIGUOUS"]),
    }


def contiguity_of_ops(arr: np.ndarray) -> dict:
    """
    Check C-contiguity for different array operations.
    """
    return {
        "row_slice": bool(arr[1:3].flags["C_CONTIGUOUS"]),
        "column_slice": bool(arr[:, 0].flags["C_CONTIGUOUS"]),
        "step_slice": bool(arr[::2].flags["C_CONTIGUOUS"]),
        "transpose": bool(arr.T.flags["C_CONTIGUOUS"]),
        "transpose_copy": bool(arr.T.copy().flags["C_CONTIGUOUS"]),
    }
