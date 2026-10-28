def is_truthy(value) -> bool:
    if value is None:
        return False

    if isinstance(value, (int, float, complex)):
        return value != 0

    if isinstance(value, str):
        return len(value) > 0

    if isinstance(value, (list, tuple, dict, set)):
        return len(value) > 0

    return True


def first_truthy(values: list):
    for value in values:
        if is_truthy(value):
            return value

    return None
