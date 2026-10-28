# Cumulative Operations & Moving Windows

Intermediate | numpy-core

Implement running and windowed statistics for a 1D series without a Python loop over positions. `running_total` is the cumulative sum, `cumulative_max` the running maximum, `consecutive_differences` the change between neighbours, `percent_change` the relative change from each value to the next (with `NaN` where the previous value is `0`), and `moving_average` the mean of every window of `w` consecutive values, computed with the cumulative-sum trick so that the cost does not grow with `w`.
