def word_frequencies(text: str) -> dict:
    frequencies = {}

    for word in text.split():
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def safe_lookup(d: dict, key, default):
    return d.get(key, default)


def increment(d: dict, key, amount: int) -> None:
    d[key] = d.get(key, 0) + amount


def dict_from_two_lists(keys: list, values: list) -> dict:
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result


def merge_prefer_second(a: dict, b: dict) -> dict:
    result = dict(a)
    result.update(b)
    return result


def merge_counts(a: dict, b: dict) -> dict:
    result = dict(a)

    for key, value in b.items():
        result[key] = result.get(key, 0) + value

    return result


def group_by_first_letter(words: list) -> dict:
    groups = {}

    for word in words:
        if word:
            key = word[0].lower()
            groups.setdefault(key, []).append(word)

    return groups


def add_defaults(config: dict, defaults: dict) -> None:
    for key, value in defaults.items():
        config.setdefault(key, value)


def remove_keys(d: dict, keys: list) -> int:
    removed = 0

    for key in keys:
        if key in d:
            del d[key]
            removed += 1

    return removed


def take_last(d: dict):
    if not d:
        return None

    return d.popitem()


def remove_and_return(d: dict, key, default):
    return d.pop(key, default)


def clear_and_report(d: dict) -> int:
    count = len(d)
    d.clear()
    return count
