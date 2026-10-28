def alias_and_call(function, value):
    """
    `function` is a function object that accepts one argument.
    Assign the function object to another local variable and call
    it with `value`. Return the function's result.

    Do not call `function` before assigning it to the local alias.

    Example:
        alias_and_call(lambda x: x * 2, 5) -> 10
    """
    alias = function
    return alias(value)


def apply_selected(functions: list, index: int, value):
    """
    `functions` is a non-empty list of one-argument function
    objects. Select the function at `index`, call it with `value`,
    and return its result.

    Negative indexes follow normal list indexing.
    """
    selected_function = functions[index]
    return selected_function(value)


def same_function(function_a, function_b) -> bool:
    """
    Return True only when `function_a` and `function_b` refer to
    the exact same function object.
    """
    return function_a is function_b


def apply_once(function, value):
    """
    Call the supplied one-argument function with `value` and
    return its result.
    """
    return function(value)


def apply_twice(function, value):
    """
    Call the supplied one-argument function twice in sequence.
    """
    return function(function(value))


def apply_n_times(function, value, count: int):
    """
    Apply the supplied one-argument function to `value` exactly
    `count` times. Negative counts return the original value.
    """
    for _ in range(count):
        value = function(value)
    return value


def transform_all(values: list, function) -> list:
    """
    Return a new list containing the result of calling `function`
    once on every element of `values`, in input order.
    """
    return [function(value) for value in values]


def make_square_function():
    """
    Return a lambda function that accepts one number and returns
    its square.
    """
    return lambda x: x * x


def make_offset_function(offset):
    """
    Return a lambda function that accepts one value and adds
    `offset` to it.
    """
    return lambda value: value + offset


def apply_lambda(values: list, function) -> list:
    """
    Return a new list containing the result of calling the supplied
    function on every element of `values`, in order.
    """
    return [function(value) for value in values]
