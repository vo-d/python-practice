def is_triangle(a, b, c):
    """This function check if the given 3 lengths
     can form a triagle

     a, b, c: integer
     """

    if c > (a + b) or b > (a + c) or a > (b + c):
        print('No')
    else:
        print('Yes')


