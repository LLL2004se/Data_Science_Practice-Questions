def analyze_route(points: list) -> tuple:
    if not points:
        return ({}, None, 0, 0, 0)

    # 1. Count visits to each point
    visit_counts = {}
    for point in points:
        if point in visit_counts:
            visit_counts[point] += 1
        else:
            visit_counts[point] = 1

    # 2. Calculate bounding box using a loop and comparisons
    min_x = max_x = points[0][0]
    min_y = max_y = points[0][1]

    for x, y in points:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    bounding_box = ((min_x, min_y), (max_x, max_y))

    # 3. Calculate Manhattan path length using an index loop
    path_length = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        path_length += abs(x2 - x1) + abs(y2 - y1)

    # 4. Calculate net displacement
    if len(points) == 1:
        net_displacement = 0
    else:
        first, *_, last = points
        net_displacement = (
            abs(last[0] - first[0]) +
            abs(last[1] - first[1])
        )

    # 5. Count revisits
    revisit_count = len(points) - len(visit_counts)

    return (
        visit_counts,
        bounding_box,
        path_length,
        net_displacement,
        revisit_count
    )
