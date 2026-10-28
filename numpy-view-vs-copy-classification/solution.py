import numpy as np


def classify_operation_result(arr: np.ndarray, operation_name: str) -> str:
    if operation_name == "basic_slice":
        result = arr[1:4]
    elif operation_name == "fancy_index":
        result = arr[[0, 2]]
    elif operation_name == "boolean_mask":
        result = arr[arr > arr.mean()]
    elif operation_name == "arithmetic":
        result = arr + 1
    elif operation_name == "explicit_array":
        result = np.array(arr)
    else:
        raise ValueError("Invalid operation_name")

    return "view" if np.shares_memory(result, arr) else "copy"
