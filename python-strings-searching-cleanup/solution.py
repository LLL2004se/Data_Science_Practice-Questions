def sentence_case(s: str) -> str:
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()


def swap_first_char_case(s: str) -> str:
    if not s:
        return ""
    return s[0].swapcase() + s[1:]


def equal_ignoring_case(a: str, b: str) -> bool:
    return a.casefold() == b.casefold()


def case_kind(s: str) -> str:
    if s.isupper():
        return "upper"
    elif s.islower():
        return "lower"
    elif s.istitle():
        return "title"
    else:
        return "mixed"


def find_all(s: str, sub: str) -> list:
    result = []

    if sub == "":
        return result

    start = 0

    while True:
        index = s.find(sub, start)

        if index == -1:
            break

        result.append(index)
        start = index + 1

    return result


def count_overlapping(s: str, sub: str) -> int:
    if sub == "":
        return 0

    count = 0
    start = 0

    while True:
        index = s.find(sub, start)

        if index == -1:
            break

        count += 1
        start = index + 1

    return count


def has_extension(filename: str, ext: str) -> bool:
    return filename.casefold().endswith("." + ext.casefold())


def classify_token(token: str) -> str:
    if token and token.isdigit():
        return "digits"
    elif token and token.isalpha():
        return "letters"
    elif token and token.isalnum():
        return "alnum"
    elif token and token.isspace():
        return "space"
    else:
        return "other"


def clean_field(s: str) -> str:
    return s.strip().rstrip(".,;").strip()


def remove_prefix_once(s: str, prefix: str) -> str:
    if s.startswith(prefix):
        return s[len(prefix):]
    return s


def replace_first_n(s: str, old: str, new: str, n: int) -> str:
    if n == 0:
        return s

    if n < 0:
        return s.replace(old, new)

    return s.replace(old, new, n)
