def square(x):
    return x * x


def min_max(values):
    minimum = maximum = values[0]

    for value in values[1:]:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    return (minimum, maximum)


def describe_pair(a, b):
    return (a + b, a - b, a * b)


def absolute_value(x):
    if x < 0:
        return -x
    return x


def percentage(value: float, total: float) -> float:
    """
    Return value / total * 100.

    The total must not be zero.

    Example:
        percentage(25, 200) -> 12.5
    """
    return value / total * 100


def repeat_text(text: str, count: int) -> str:
    """
    Return `text` repeated `count` times.

    `count` is expected to be non-negative.

    Example:
        repeat_text("ab", 3) -> "ababab"
    """
    return text * count


def make_pair(first, second) -> tuple:
    """
    Return a 2-element tuple `(first, second)`.

    The two values are returned in the same order they were
    supplied.

    Example:
        make_pair(1, "x") -> (1, "x")
    """
    return (first, second)


def function_metadata():
    return {
        "doc": function_metadata.__doc__,
        "annotations": function_metadata.__annotations__
    }
