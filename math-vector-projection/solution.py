import numpy as np


def project(a, b):
    return (np.dot(a, b) / np.dot(b, b)) * b


def orthogonal_component(a, b):
    return a - project(a, b)
