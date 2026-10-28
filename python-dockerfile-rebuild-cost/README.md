# Order a Dockerfile for the Build Cache

Advanced | python-packaging | containerization | docker | build-cache | optimization

Write `rebuild_cost(dockerfile, changed)`, which computes how long a rebuild takes given which source files changed, then use it to see why copying `requirements.txt` before the rest of the source makes rebuilds fast.
