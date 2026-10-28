import hashlib


def build_manifest(files: dict[str, bytes]) -> dict:
    """
    `files` maps a relative path to that file's bytes.

    Return a dict with:
      "entries": a list of {"path": path, "sha256": hex digest of the
                 file's bytes}, sorted by path
      "nfiles":  the number of files
      "size":    the total number of bytes across all files
      "digest":  the SHA-256 hex digest of this exact text, encoded as
                 UTF-8: one line "<path>\t<sha256>" per entry, in sorted
                 order, joined with "\n" (no trailing newline).
                 An empty directory hashes the empty string.
    """
    entries = []
    total_size = 0

    for path in sorted(files):
        content = files[path]
        file_digest = hashlib.sha256(content).hexdigest()

        entries.append({
            "path": path,
            "sha256": file_digest
        })

        total_size += len(content)

    # Build the manifest text without a trailing newline.
    manifest_text = "\n".join(
        f"{entry['path']}\t{entry['sha256']}"
        for entry in entries
    )

    manifest_digest = hashlib.sha256(
        manifest_text.encode("utf-8")
    ).hexdigest()

    return {
        "entries": entries,
        "nfiles": len(files),
        "size": total_size,
        "digest": manifest_digest
    }
