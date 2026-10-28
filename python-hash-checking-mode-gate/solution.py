def check_hash_mode(requirements: list[dict]) -> list[str]:
    """
    Each requirement is a dict with keys "name", "spec" (e.g. "==1.2.3",
    ">=2.0", or "") and "hashes" (a possibly empty list of strings).

    Hash-checking mode is ACTIVE if at least one requirement has a
    non-empty "hashes" list. If it is not active, return [].

    If it is active, every requirement must be:
      - pinned: its spec starts with "==" and contains no "*"
      - hashed: its "hashes" list is non-empty
    Return one error string per violation, in the form
      "<name>: not pinned"   or   "<name>: missing hash"
    ordered by requirement name, and for one requirement "not pinned"
    before "missing hash". Return [] when there are no violations.
    """
    # Check whether hash-checking mode is active.
    if not any(req["hashes"] for req in requirements):
        return []

    errors = []

    # Sort requirements alphabetically by name.
    for req in sorted(requirements, key=lambda r: r["name"]):
        name = req["name"]
        spec = req["spec"]
        hashes = req["hashes"]

        # Check whether the requirement is pinned.
        if not spec.startswith("==") or "*" in spec:
            errors.append(f"{name}: not pinned")

        # Check whether the requirement has hashes.
        if not hashes:
            errors.append(f"{name}: missing hash")

    return errors
