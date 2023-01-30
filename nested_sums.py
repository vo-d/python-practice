def nested_sum(lists):
    """This function add up sum of each list 
    member
    
    lists: array of list
    Return: number
    """
    total = 0
    for list in lists:
        total += sum(list)
    return total