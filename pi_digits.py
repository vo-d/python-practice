import numpy as np
import math

def digits():
    """
    This function creates a numpy array which hold 16 digit of pi
    """
    pi_string = str(math.pi)
    pi_string = pi_string.replace(".","")
    first_16 = np.empty(16, dtype = "int")
    for i in range(len(pi_string)):
        first_16[i] = int(pi_string[i])
    return first_16

def test_digits():
    """
    This funciton test the digits() function
    """
    assert np.all(digits() == [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3])

if __name__ == "__main__":
    print(digits())
    test_digits()