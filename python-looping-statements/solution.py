def countdown_with_skip(start: int) -> list:
    result = []
    while start >= 1:
        if start == 3:
            start -= 1
            continue
        result.append(start)
        start -= 1
    return result


def find_first_negative(numbers: list) -> int | None:
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            result = numbers[i]
            break
        i += 1
    else:
        return None

    return result


def sum_with_index(numbers: list) -> dict:
    result = {}
    running_sum = 0

    for index, number in enumerate(numbers):
        running_sum += number
        result[index] = running_sum

    return result


def manual_iteration_trace(items: list) -> list:
    result = []
    iterator = iter(items)

    while True:
        try:
            item = next(iterator)
            result.append(item)
        except StopIteration:
            break

    return result
