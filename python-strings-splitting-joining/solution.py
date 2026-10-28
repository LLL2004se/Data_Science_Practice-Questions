def word_count(text: str) -> int:
    return len(text.split())


def reverse_word_order(text: str) -> str:
    words = text.split()
    return " ".join(words[::-1])


def last_field(line: str, sep: str) -> str:
    return line.rsplit(sep, 1)[-1]


def count_nonblank_lines(text: str) -> int:
    count = 0

    for line in text.splitlines():
        if line.strip():
            count += 1

    return count


def make_csv_line(fields) -> str:
    result = []

    for field in fields:
        if "," in field:
            field = '"' + field + '"'
        result.append(field)

    return ",".join(result)
