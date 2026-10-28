# Descriptive Statistics

Intermediate | numpy-core

Implement the summary statistics an analyst reaches for first, from their definitions. `percentiles` returns chosen percentiles of a sample (linear interpolation), `iqr` the interquartile range, `zscores` standardises a sample to mean 0 and standard deviation 1, `pearson` is the Pearson correlation of two samples computed from its formula (without calling `np.corrcoef`), and `covariance_matrix` is the sample covariance matrix of the columns of a 2D array (without calling `np.cov`).
