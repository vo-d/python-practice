import numpy as np

def binary():
    """
    This function creates a array with the integer 2 and store as unsigned 64-bit integer.
    Then puts 2 ^ 63-1 and calls a numpy method which will return the binary value
    of 2 ^ 63-1.

    return: int
    """
    array = np.array(2, dtype="int64")
    array = array**63-1
    return(int(np.binary_repr(array)))

def test_binary():
    """
    This function test the binary() function
    """
    assert binary() == 111111111111111111111111111111111111111111111111111111111111111
    assert binary() != "111111111111111111111111111111111111111111111111111111111111111"
    assert binary() != 1

if __name__ == "__main__":
    print(binary())
    test_binary()