import numpy as np


def trace(A):
    return np.sum(np.diag(A))


def trace_of_product(A, B):
    return np.sum(A * B.T)
