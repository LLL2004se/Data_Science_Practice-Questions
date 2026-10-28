# Verify an Artifact Against Allowed Hashes

Intermediate | python-packaging | reproducible-environments | hashing | supply-chain

Write `verify_artifact(data, allowed)`, which checks the bytes of a downloaded package file against the list of hashes a lock or requirements file allows, the core check behind pip's `--require-hashes` mode.
