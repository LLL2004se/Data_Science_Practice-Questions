# Assemble: Leaderboard Queries

Intermediate | numpy-core

A game keeps one score per player in an array. Implement the four queries a leaderboard needs, using sorting and partial sorting rather than Python loops. `top_k` returns the indices of the `k` highest scores (highest first, ties by lower index), `competition_ranks` gives every player a 1-based rank where equal scores share the best rank ("1, 2, 2, 4"), `kth_largest` returns the `k`-th largest value without sorting the whole array, and `percentile_rank` reports what fraction of the scores each player strictly beats.
