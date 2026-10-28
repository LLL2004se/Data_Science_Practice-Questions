def _version_key(version: str) -> tuple:
    return tuple(int(part) for part in version.split("."))


def stale_packages(declared: dict[str, str], locked: dict[str, str]) -> list[str]:
    """
    `declared` maps package name -> minimum allowed version ("2.0",
    "1.10.3", ...), meaning "version >= minimum".
    `locked` maps package name -> the one exact locked version.

    Return the sorted names of declared packages that the lock does NOT
    satisfy: the package is missing from `locked`, or its locked version
    is lower than the declared minimum.

    Versions are dotted integers compared numerically per component
    ("1.10" > "1.9"), and "1.2" equals "1.2.0".
    Packages in `locked` that are not declared (transitive dependencies)
    are ignored. Return [] when the lock is current.
    """
    stale = []

    for package, minimum_version in declared.items():
        if package not in locked:
            stale.append(package)
            continue

        declared_key = _version_key(minimum_version)
        locked_key = _version_key(locked[package])

        # Pad shorter versions with zeros, so 1.2 == 1.2.0.
        length = max(len(declared_key), len(locked_key))
        declared_key += (0,) * (length - len(declared_key))
        locked_key += (0,) * (length - len(locked_key))

        if locked_key < declared_key:
            stale.append(package)

    return sorted(stale)
