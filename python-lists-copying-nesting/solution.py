import copy


def shallow_copy(lst: list) -> list:
    return lst.copy()


def deep_copy(nested: list) -> list:
    return copy.deepcopy(nested)


def shares_inner_objects(original: list, duplicate: list) -> bool:
    return all(a is b for a, b in zip(original, duplicate))


def add_row_safely(matrix: list, row: list) -> list:
    return copy.deepcopy(matrix) + [copy.deepcopy(row)]


def make_grid(rows: int, cols: int, fill) -> list:
    return [[fill for _ in range(cols)] for _ in range(rows)]


def rows_are_independent(grid: list) -> bool:
    return len({id(row) for row in grid}) == len(grid)


def transpose(matrix: list) -> list:
    return [list(row) for row in zip(*matrix)]
