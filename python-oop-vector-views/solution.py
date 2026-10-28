import math


class Vector:
    """
    A one-dimensional sequence of numbers that can be a view onto
    shared data.

    __init__(self, buffer, indices=None):
        Store `buffer` (a list; do NOT copy it) in self.buffer.
        Store `indices` (a range of buffer positions) in
        self.indices; if None, use range(len(buffer)).

    __len__(self):
        Number of positions exposed.

    __getitem__(self, key):
        int   -> the element at that position of the view
                 (negative allowed; out of range raises
                 IndexError).
        slice -> a NEW Vector that is a VIEW of the same buffer
                 (indices = self.indices[key]).

    __setitem__(self, key, value):
        int   -> write `value` into the buffer at that position.
        slice -> `value` is either a single number, written to
                 EVERY selected position, or a sequence (anything
                 with a length) whose elements are written to the
                 selected positions in order. Take a snapshot
                 list of a sequence value BEFORE writing, so
                 overlapping source and target cannot corrupt
                 each other. The lengths must match for a
                 sequence value.
        Writes go into the buffer and are visible through every
        view of it.

    to_list(self):
        A NEW list of the exposed values.

    copy(self):
        A NEW Vector that owns a NEW buffer holding the exposed
        values (independent of this one).

    map(self, func):
        A NEW Vector (new buffer) holding func(x) for every
        exposed x.

    __add__(self, other):
        `other` is either a number (add it to every element) or a
        sequence with a length, such as another Vector or a list
        (add element-wise; equal lengths). Return a NEW Vector
        with a NEW buffer. Decide scalar vs sequence with
        hasattr(other, "__len__"), not isinstance.

    __radd__(self, other):
        Return self + other, so sum([...vectors...]) works.

    normalize_(self, eps=1e-5):
        Layer-normalize the exposed values IN PLACE: with
        mean = sum/n and variance = sum((x - mean)**2)/n, write
        (x - mean) / sqrt(variance + eps) back into the buffer
        at the exposed positions. Positions outside the view are
        untouched. Return self. An empty view does nothing.

    __repr__(self):
        "Vector(" + repr(self.to_list()) + ")",
        for example "Vector([1, 2, 3])".
    """

    def __init__(self, buffer, indices=None):
        self.buffer = buffer
        self.indices = range(len(buffer)) if indices is None else indices

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return Vector(self.buffer, self.indices[key])
        return self.buffer[self.indices[key]]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            selected_indices = list(self.indices[key])

            if hasattr(value, "__len__"):
                values = list(value)

                if len(values) != len(selected_indices):
                    raise ValueError(
                        "attempt to assign sequence of different size to slice"
                    )

                for index, item in zip(selected_indices, values):
                    self.buffer[index] = item
            else:
                for index in selected_indices:
                    self.buffer[index] = value
        else:
            self.buffer[self.indices[key]] = value

    def to_list(self):
        return [self.buffer[index] for index in self.indices]

    def copy(self):
        return Vector(self.to_list())

    def map(self, func):
        return Vector([func(value) for value in self])

    def __add__(self, other):
        values = self.to_list()

        if hasattr(other, "__len__"):
            other_values = list(other)

            if len(values) != len(other_values):
                raise ValueError("vectors must have equal lengths")

            result = [
                a + b for a, b in zip(values, other_values)
            ]
        else:
            result = [value + other for value in values]

        return Vector(result)

    def __radd__(self, other):
        return self + other

    def normalize_(self, eps=1e-5):
        values = self.to_list()

        if not values:
            return self

        mean = sum(values) / len(values)
        variance = sum(
            (value - mean) ** 2 for value in values
        ) / len(values)

        denominator = math.sqrt(variance + eps)

        for i, value in enumerate(values):
            self[i] = (value - mean) / denominator

        return self

    def __repr__(self):
        return "Vector(" + repr(self.to_list()) + ")"
