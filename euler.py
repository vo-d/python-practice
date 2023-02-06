import math
import sys


def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def term(k):
    return 1 / factorial(k)


def terms(k):
    for k in range(1_000):
        yield term(k)


def estimate_euler():
    """Computes an estimate of e.
    
    """
    SUM = 0

    epsilon = sys.float_info.epsilon
    for term in terms:
        if term < epsilon:
            break
        sum += term
        if abs(SUM) < epsilon:
            break
    return SUM

print(estimate_euler())