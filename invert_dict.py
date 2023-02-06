import collections


def invert_dict(d):
    """This function invert a dictionary and return a 
    dictionary-like object

    d: dictionary
    Returns: object
    """
    inverse = collections.defaultdict(list)
    for key in d:
        val = d[key]
        inverse[val].append(key)
    return inverse
    

