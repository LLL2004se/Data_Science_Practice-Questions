def make_singleton(x) -> tuple:
    return (x,)


def tuple_replace(t: tuple, index: int, value) -> tuple:
    if -len(t) <= index < len(t):
        index %= len(t)
        return t[:index] + (value,) + t[index + 1:]
    return t


def count_and_first_index(t: tuple, x) -> tuple:
    count = t.count(x)
    first_index = t.index(x) if x in t else -1
    return (count, first_index)


def freeze_rows(matrix: list) -> tuple:
    return tuple(tuple(row) for row in matrix)


def thaw_rows(frozen: tuple) -> list:
    return [list(row) for row in frozen]


def updated(seq, index: int, value):
    if isinstance(seq, list):
        result = seq.copy()
        if -len(result) <= index < len(result):
            result[index] = value
        return result

    elif isinstance(seq, tuple):
        if -len(seq) <= index < len(seq):
            index %= len(seq)
            return seq[:index] + (value,) + seq[index + 1:]
        return seq

    raise TypeError("seq must be a list or tuple")


def has_mutable_element(t: tuple) -> bool:
    return any(isinstance(item, (list, dict, set)) for item in t)

def head_and_tail(seq) -> tuple:
    if len(seq) == 0:
        return (None, [])
    return (seq[0], list(seq[1:]))


def rotate_three(a, b, c) -> tuple:
    return (b, c, a)


def sum_pairs(pairs: list) -> list:
    return [a + b for a, b in pairs]


def ends_and_middle(seq) -> tuple:
    if len(seq) == 0:
        return (None, [], None)

    first = seq[0]
    last = seq[-1]

    middle = list(seq[1:-1])

    return (first, middle, last)
