def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def n_choose_k(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
