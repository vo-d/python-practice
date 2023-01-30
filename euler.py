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



def estimate_euler():
    """Computes an estimate of e.
    
    """

    epsilon = sys.float_info.epsilon
    total = 0
    k = 0
    e = 1
    while True:
        total += (e**k)/(factorial(k))

        if abs(total) < 1e-15:
            break
        k += 1
    return total**(1/e)

print(estimate_euler())