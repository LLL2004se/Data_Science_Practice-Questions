def is_subset(a, b):
    return a.issubset(b)


def argmax(values):
    max_index = 0
    max_value = values[0]

    for i in range(1, len(values)):
        if values[i] > max_value:
            max_value = values[i]
            max_index = i

    return max_index
