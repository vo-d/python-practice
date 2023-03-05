import numpy as np


def sphere_volumes(r_array):
    """This function get a NumPy array of radiuses and return 
    a NumPy array of sphere volumns on the given radiuses

    r_array: NumPy array
    returns: NumPy array
    """
    volume = 4/3 * np.pi * r_array ** 3
    return volume

