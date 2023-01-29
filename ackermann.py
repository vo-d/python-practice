def ack (m, n):
    """This function evaluate Ackermann funciton A(m,n)
    
    n, m: non-negative integers
    """
    if m == 0:
        return n + 1
    if n == 0:
        return ack (m - 1, 1)
    else:
        return ack (m - 1, ack (m, n - 1))


print(ack (3, 4))