import numpy as np
import sys


def mc_pi_numpy(max_iterations=200):
    """
        This function uses NumPy to generate random points within a square 
        and estimate the value of pi by counting the fraction of points 
        that lie inside a unit circle.
    """
    inside_unit_circle = total_points = 0
    while True:
        total_points += 1
        points = np.random.rand(2, max_iterations)
        inside_unit_circle += np.sum(np.sqrt(points[0]**2 + points[1]**2) < 1)
        yield 4 * inside_unit_circle / (total_points * max_iterations)


def main(max_iterations=200):
    """
    This function takes an optional argument max_iterations and calls the 
    mc_pi_numpy function to estimate pi for max_iterations iterations. The 
    function prints the successive estimates of pi until it reaches max_iterations.
    """
    for i, pi in enumerate(mc_pi_numpy(max_iterations=max_iterations)):
        if i > max_iterations:
            break
    print(pi)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()