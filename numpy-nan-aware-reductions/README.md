# NaN-aware Reductions

Beginner | numpy-core

Real arrays have holes, marked `NaN`, and one `NaN` turns a plain `sum`, `mean` or `max` into `NaN`. Implement the tools that work around holes. `summary_ignoring_nan` reports the count, mean, standard deviation, minimum and maximum of the known values, `count_missing` counts the holes along an axis, `fill_with_column_means` replaces each hole with the mean of the other values in its column, `rows_without_nan` keeps only complete rows, and `argmax_ignoring_nan` returns the position of the largest known value.
