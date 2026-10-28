def first_and_last(s: str) -> str:
    if s == "":
        return ""
    return s[0] + s[-1]


def reverse_string(s: str) -> str:
    return s[::-1]


def every_kth_from(s: str, start: int, k: int) -> str:
    if start < -len(s) or start >= len(s):
        return ""
    return s[start::k]
