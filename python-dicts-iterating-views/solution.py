def sum_of_values(d: dict) -> int:
    return sum(d.values())


def keys_with_max_value(d: dict) -> list:
    if not d:
        return []

    max_value = max(d.values())
    return [key for key, value in d.items() if value == max_value]


def remove_where_value_below(d: dict, threshold: int) -> None:
    for key in list(d.keys()):
        if d[key] < threshold:
            del d[key]


def value_of(pair: tuple):
    return pair[1]


def items_by_value_desc(d: dict) -> list:
    result = sorted(d.items())
    result = sorted(result, key=value_of, reverse=True)
    return result
