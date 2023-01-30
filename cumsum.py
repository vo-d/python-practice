def cumsum(list):
    """This function create a new list that 
    ith element is the sum of the fisrt i+1 
    elememtns from the original list
    
    list: array
    """
    sums = []
    total = 0
    for i in list:
        total += i
        sums.append(total)
    print(sums)

