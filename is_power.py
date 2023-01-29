def is_power(a, b):
    """This function will check if a is a power of b or not
    
    a, b: integer
    """
    while a % b == 0:
        if a == b: 
            return True
        else:
            a = a / b
    return False
