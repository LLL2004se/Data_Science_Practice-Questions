def run_pipeline(values: list, *transformations, **options) -> list:
    """
    Apply a sequence of transformation functions to every value
    in `values` and return the resulting values as a new list.

    Each transformation must accept one value and return one value.
    Transformations are applied in the order supplied.

    Supported keyword options:

        unique
            Boolean. If True, include each final output value only
            once, preserving the order of its first occurrence.
            Defaults to False.

        limit
            Integer or None. If an integer is supplied, stop after
            collecting at most `limit` output values. Defaults to
            None, meaning no limit. `limit` must not be negative.

    Unknown keyword options must raise `TypeError`.

    If `unique=True`, use a set to track values already emitted
    and a list to preserve the output order.

    If `limit == 0`, return an empty list.

    The input `values` must not be modified.
    """
    unknown_options = set(options) - {"unique", "limit"}
    if unknown_options:
        raise TypeError(f"Unexpected keyword option: {next(iter(unknown_options))}")

    unique = options.get("unique", False)
    limit = options.get("limit", None)

    if limit is not None:
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError("limit must be an integer or None")
        if limit < 0:
            raise ValueError("limit must not be negative")

    if limit == 0:
        return []

    result = []
    seen = set()

    for value in values:
        transformed = value

        for transformation in transformations:
            transformed = transformation(transformed)

        if unique:
            if transformed in seen:
                continue
            seen.add(transformed)

        result.append(transformed)

        if limit is not None and len(result) >= limit:
            break

    return result
