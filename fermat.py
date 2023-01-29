def check_fermat(a, b, c, n):
    """This function check Fermat's Last Theorem

    a, b, c, n: integer
    """
    if n > 2 and (a ** n + b ** n == c ** n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")