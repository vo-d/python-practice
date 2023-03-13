from __future__ import print_function, division
import numpy as np

def factorial(n):
    """
    This funtion is supposed to computes factorial of n recursively

    n: integer
    return: integer
    """
    return 1 if n == 0 else n * factorial(n-1)

def estimate_pi(maxk):
    """
    This function get the maxk value and compute pi base on the given maxk

    maxk: integer
    return: float
    """
    k = np.arange(maxk)
    factor = 2 * np.sqrt(2) / 9801
    num = factorial(4*k) * (1103 + 26390*k)
    den = factorial(k)**4 * 396**(4*k)
    total = np.sum(num / den)
    return 1 / (factor * total)

