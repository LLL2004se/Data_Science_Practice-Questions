def edge_key(a: int, b: int) -> tuple:
    return (min(a, b), max(a, b))


def count_visits(path: list) -> dict:
    counts = {}

    for point in path:
        if point in counts:
            counts[point] += 1
        else:
            counts[point] = 1

    return counts


def group_points_by_cell(points: list, cell_size: int) -> dict:
    groups = {}

    for x, y in points:
        key = (x // cell_size, y // cell_size)

        if key not in groups:
            groups[key] = []

        groups[key].append((x, y))

    return groups
