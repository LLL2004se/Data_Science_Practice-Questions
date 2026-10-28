def first_positions(words: list) -> dict:
    positions = {}

    for i, word in enumerate(words):
        if word not in positions:
            positions[word] = i

    return positions


def same_key(a, b) -> bool:
    return hash(a) == hash(b) and a == b


def distinct_key_count(keys: list) -> int:
    dictionary = {}

    for key in keys:
        dictionary[key] = None

    return len(dictionary)
