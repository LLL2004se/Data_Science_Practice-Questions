import numpy as np


def clean_and_reorder(data: np.ndarray, row_range: tuple, priority_indices: list) -> dict:
    # Step 1: Extract the rows using slicing
    region = data[row_range[0]:row_range[1], :]

    # Step 2: Replace negative values with 0 without modifying region
    cleaned = np.where(region < 0, 0, region)

    # Step 3: Reorder columns using fancy indexing
    reordered = cleaned[:, priority_indices]

    # Return the results
    return {
        "region": region,
        "cleaned": cleaned,
        "reordered": reordered,
        "region_shares_memory_with_data": np.shares_memory(region, data),
        "cleaned_shares_memory_with_region": np.shares_memory(cleaned, region)
    }
