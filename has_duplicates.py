def has_duplicates(list):
    """This function will take a list and return 
    True if there is any element that apears more 
    than once

    list: list
    return: boolean
    """
    # make a copy of t to avoid modifying the list
    list_copy = list[:]
    list_copy.sort()

    # check for adjacent elements that are equal
    for i in range(len(list_copy)-1):
        if list_copy[i] == list_copy[i+1]:
            return True
    return False