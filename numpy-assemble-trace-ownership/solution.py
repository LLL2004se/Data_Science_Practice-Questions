import numpy as np


def trace_pipeline(arr: np.ndarray) -> dict:
    # Step 1: Basic slice (view)
    step_a = arr[2:9]

    # Step 2: Fancy indexing (copy)
    step_b = step_a[[0, 2, 4]]

    # Step 3: Explicit copy
    step_c = step_a.copy()

    # Save original values to check whether mutation affects copies
    step_b_first_before = step_b[0]
    step_c_first_before = step_c[0]

    # Step 4: Mutate the view
    step_a[0] = -1

    # Find the ultimate owner using the .base chain
    owner = step_a
    while owner.base is not None:
        owner = owner.base

    return {
        "step_a": step_a,
        "step_b": step_b,
        "step_c": step_c,
        "arr_after_mutation": arr,
        "step_a_shares_memory_with_arr": bool(np.shares_memory(step_a, arr)),
        "step_b_shares_memory_with_arr": bool(np.shares_memory(step_b, arr)),
        "step_c_shares_memory_with_arr": bool(np.shares_memory(step_c, arr)),
        "step_a_ultimate_owner_is_arr": owner is arr,
        "arr_reflects_mutation": bool(arr[2] == -1),
        "step_b_reflects_mutation": bool(step_b[0] != step_b_first_before),
        "step_c_reflects_mutation": bool(step_c[0] != step_c_first_before)
    }
