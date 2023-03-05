import numpy as np


# Create NumPy arrays for the original problem
prices = np.array([24.95])
discounts = np.array([0.4])
shipping_base = np.array([3])
shipping_additional = np.array([0.75])
quantities = np.array([60])


# Add 2 more books to the order
prices = np.concatenate([prices , [26.95, 27.95]])
discounts = np.concatenate([discounts, [0.35, 0.45]])
shipping_base = np.concatenate([shipping_base, [4, 5]])
shipping_additional = np.concatenate([shipping_additional, 
                                        [1.0, 1.25]])
quantities = np.concatenate([quantities, [70, 80]])


def wholesale_books(prices, discounts, shipping_base, 
                        shipping_additional, 
                        number_of_copies):
    """This function get NumPy arrays of price, 
    discount, base shipping cost, additional shipping cost, 
    number of copies and return a NumPy array of sphere 
    volumns on the given radiuses

    prices: NumPy array
    discounts: NumPy array
    shipping_base: NumPy array
    shipping_additional: NumPy array
    number_of_copies: NumPy array

    return: NumPy array
    """
    discounted_price = prices * (1 - discounts)

    shipping_cost = shipping_base + (shipping_additional * \
    (number_of_copies - 1))

    total_cost = (discounted_price * number_of_copies) + \
    shipping_cost

    return total_cost