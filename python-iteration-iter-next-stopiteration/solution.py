def consume_iterator(iterable) -> list:
    """
    Obtain an iterator from `iterable` and manually consume it
    using `next()` until `StopIteration`.

    Return a new list containing all values in the original
    iteration order.

    Do not use a `for` loop.

    Example:
        consume_iterator([1, 2, 3]) -> [1, 2, 3]
        consume_iterator([]) -> []
    """
    iterator = iter(iterable)
    result = []

    while True:
        try:
            value = next(iterator)
            result.append(value)
        except StopIteration:
            break

    return result


def take_first(iterable, count: int) -> list:
    """
    Obtain an iterator from `iterable` and consume at most
    `count` values using `next()`.

    If the iterable becomes exhausted before `count` values are
    produced, stop early.

    If `count <= 0`, return an empty list.

    Example:
        take_first([10, 20, 30], 2) -> [10, 20]
        take_first([10], 5) -> [10]
    """
    iterator = iter(iterable)
    result = []

    while len(result) < count:
        try:
            result.append(next(iterator))
        except StopIteration:
            break

    return result


def next_or_default(iterator, default):
    """
    Call `next()` on the supplied iterator.

    Return the next value if one exists. If the iterator is
    exhausted, return `default`.

    Do not treat a produced value such as None, 0, or False as
    exhaustion.
    """
    try:
        return next(iterator)
    except StopIteration:
        return default
