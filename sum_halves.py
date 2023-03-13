import numpy as np

def calculate_sum():
    """
    This function create a numpy array from 1-100 of type float64 then
    get the value in the array times it by 2 and then divide 1 by
    that outcome and overwrite the value in the original array. After
    that, the function return the sum of all item in the np array

    return: float
    """
    sum_array = np.arange(1, 100, dtype="float64")
    sum_array = 1/(sum_array * 2)
    return sum_array.sum()
    
def test_calculate_sum():
    """
    This function test the calculate_sum() function"""
    assert calculate_sum() == 2.5886887588198104
    assert calculate_sum() != 2.5
    assert calculate_sum() != "2.543634634643"

if __name__ == "__main__":
    print(calculate_sum())
    test_calculate_sum()