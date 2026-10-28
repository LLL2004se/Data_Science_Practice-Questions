def compare_strings(a: str, b: str) -> int:
    min_len = min(len(a), len(b))

    for i in range(min_len):
        if ord(a[i]) < ord(b[i]):
            return -1
        elif ord(a[i]) > ord(b[i]):
            return 1

    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1

    return 0


def compare_ignoring_case(a: str, b: str) -> int:
    a = a.casefold()
    b = b.casefold()

    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


def caesar_shift(s: str, k: int) -> str:
    result = []
    k %= 26

    for ch in s:
        if 'a' <= ch <= 'z':
            shifted = (ord(ch) - ord('a') + k) % 26
            result.append(chr(ord('a') + shifted))
        elif 'A' <= ch <= 'Z':
            shifted = (ord(ch) - ord('A') + k) % 26
            result.append(chr(ord('A') + shifted))
        else:
            result.append(ch)

    return "".join(result)


def utf8_byte_length(s: str) -> int:
    return len(s.encode("utf-8"))


def roundtrip(s: str, encoding: str) -> str:
    encoded = s.encode(encoding, errors="replace")
    return encoded.decode(encoding)


def is_ascii_only(s: str) -> bool:
    return len(s) == len(s.encode("utf-8"))


def first_byte_values(s: str, count: int):
    return list(s.encode("utf-8")[:count])
