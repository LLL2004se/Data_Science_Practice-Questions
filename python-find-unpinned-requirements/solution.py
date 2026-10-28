import re

_PINNED = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._-]*(\[[^\]]*\])?\s*==\s*[^\s*,=<>!~]+$"
)


def find_unpinned(requirements: list[str]) -> list[str]:
    """
    `requirements` is the list of lines of a requirements.txt file.
    Return, in their original order, the requirements that are NOT
    pinned to an exact version.

    Clean each line before judging it:
      - a line that is blank, or starts with `#`, is ignored
      - cut off an inline comment (everything from " #")
      - cut off options (everything from " --", e.g. " --hash=...")
      - remove a trailing backslash continuation
      - remove an environment marker (everything from ";")
      - a cleaned line that is empty or starts with "-" (such as
        "--require-hashes") is ignored

    A cleaned requirement is pinned if it is `name==version` (optionally
    `name[extra]==version`) where the version has no `*` and no `,`, or
    if it is a direct reference containing " @ ".

    Return the cleaned text of each unpinned requirement.
    """
    unpinned = []

    for line in requirements:
        line = line.strip()

        # Ignore blank lines and full-line comments.
        if not line or line.startswith("#"):
            continue

        # Remove inline comments.
        line = line.split(" #", 1)[0]

        # Remove options such as --hash.
        line = line.split(" --", 1)[0]

        # Remove a trailing continuation backslash.
        line = line.rstrip().removesuffix("\\").strip()

        # Remove environment markers.
        line = line.split(";", 1)[0].strip()

        # Ignore empty lines and requirement-file options.
        if not line or line.startswith("-"):
            continue

        # Direct references are considered pinned.
        if " @ " in line:
            continue

        # Exact versions are pinned only if there is no wildcard.
        if _PINNED.fullmatch(line) and "*" not in line:
            continue

        unpinned.append(line)

    return unpinned
