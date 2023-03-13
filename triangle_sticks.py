import numpy as np

def are_triangles(arr):
    """This function check if the given 3 lengths in 
    each NumPy array can form a triagle

    arr: NumPy array
    return: NumPy array
     """
    # Calculate the sum of each row
    row_sum = np.sum(arr, axis=1)

    """ Check if the sum of any two columns is greater 
    than the third column """
    result = (row_sum - arr[:, 0] > arr[:, 0]) & \
    (row_sum - arr[:, 1] > arr[:, 1]) & \
    (row_sum - arr[:, 2] > arr[:, 2])
    
    return result


def test_are_triangles():
    """ This is a test that can be used to test 
    are_triangle function
    """
    # Define test cases
    test_case_1 = np.array([[1, 2, 3], 
                            [4, 5, 6], 
                            [7, 8, 9]])

    test_case_2 = np.array([[1, 2, 4], 
                            [2, 5, 7], 
                            [10, 20, 30], 
                            [50, 50, 99]])

    # Test the are_triangles function 
    result_1 = are_triangles(test_case_1)
    result_2 = are_triangles(test_case_2)

    # Verify the results
    expected_1 = np.array([False, True, True])
    expected_2 = np.array([False, False, False, True])
    assert np.array_equal(result_1, expected_1)
    assert np.array_equal(result_2, expected_2)
