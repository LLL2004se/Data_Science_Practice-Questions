def square_map(n: int) -> dict:
    return {i: i * i for i in range(1, n + 1)}


def invert(d: dict) -> dict:
    return {value: key for key, value in d.items()}


def filter_items(d: dict, min_value: int) -> dict:
    return {
        key: value
        for key, value in d.items()
        if value >= min_value
    }


def dict_from_parallel(keys: list, values: list) -> dict:
    return {key: value for key, value in zip(keys, values)}


def nested_get(d: dict, path: list, default):
    current = d

    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]

    return current


def nested_set(d: dict, path: list, value) -> None:
    current = d

    for key in path[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]

    current[path[-1]] = value


def flatten_two_levels(d: dict) -> dict:
    return {
        f"{outer}.{inner}": value
        for outer, inner_dict in d.items()
        for inner, value in inner_dict.items()
    }
