import copy


def label_of(row: list) -> str:
    return row[0]


def quantity_of(row: list) -> int:
    return row[1]


def process_inventory(rows: list, min_qty: int) -> list:
    # 1. Create an independent deep copy
    snapshot = copy.deepcopy(rows)

    # 2. Remove rows with quantity below min_qty in place
    rows[:] = [row for row in rows if quantity_of(row) >= min_qty]

    # 3. Sort using two stable sort passes
    # Least important key first: label ascending
    rows.sort(key=label_of)

    # Most important key second: quantity descending
    rows.sort(key=quantity_of, reverse=True)

    # 4. Get labels of the first three rows
    top_labels = [label_of(row) for row in rows[:3]]

    # 5. Get quantities of all remaining rows
    quantities = [quantity_of(row) for row in rows]

    return [snapshot, top_labels, quantities]
