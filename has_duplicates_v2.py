def has_duplicates2(list):
    """This function convert the list input to a set of 
    no duplicated variable

    Since set has no duplicated value, it will be shorter 
    than the input list if the list has any duplication
    
    list: list
    """
    return len(set(list)) < len(list)