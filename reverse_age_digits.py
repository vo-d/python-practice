def check_reverse(a, b):
    """Returns a boolen answering if the two ages are 
    palindrome
    
    a, b: integer
    returns: boolean
    """
    return str(a).zfill(2) == str(b).zfill(2)[::-1]


def check_past(a, b):
    """Print all the pair of ages that was palindrome 
    in the past 
    before the given ages
    
    a, b: int
    """
    while(a > 0):
        a -= 1
        b -= 1
        if check_reverse(a, b):
            print(a, b)
        

def check_future(a, b):
    """Print all the pair of ages that will be 
    palindrome
    in the future after the given ages
    
    a, b: int
    """
    while(b < 100):
        if check_reverse(a, b):
            print (a, b)
        a += 1
        b+= 1


def check_diffs(a, b):
    """Print all the pair of ages that are palindrome 
    in both the past and the future
    If a > b, then we swap a and b position
    
    a, b: int
    """
    if a > b:
        c = a
        a = b
        b = c
    check_past(a, b)
    check_future(a, b)


check_diffs(35, 53)