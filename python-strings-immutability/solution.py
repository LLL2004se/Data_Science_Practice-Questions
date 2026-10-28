def replace_char_at(s: str, index: int, ch: str) -> str:
    if index < -len(s) or index >= len(s):
        return s

    index = index % len(s)
    return s[:index] + ch + s[index + 1:]


def insert_at(s: str, index: int, text: str) -> str:
    if index < 0:
        index = max(0, len(s) + index)
    else:
        index = min(index, len(s))

    return s[:index] + text + s[index:]


def join_with_separator(parts, sep: str) -> str:
    result = ""

    for i in range(len(parts)):
        if i > 0:
            result += sep
        result += parts[i]

    return result


def repeat_text(s: str, n: int) -> str:
    return s * n if n > 0 else ""


def total_chars_copied(n: int, piece_length: int) -> int:
    if n <= 0:
        return 0

    return piece_length * n * (n + 1) // 2
