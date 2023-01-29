def first(word):
    """This function returns the first character 
    of a string
    
    word: string
    """
    return word[0]


def last(word):
    """This function returns the last character 
    of a string
    
    word: string
    """    
    return word[-1]


def middle(word):
    """This function returns a string that is between 
    the first and the last character of the string
    
    word: string
    """    
    return word[1:-1]


"""Part 1
If I call middle with a string with two letters it 
will return a string with no character.The same thing 
will happen if I call middle with a string with one 
letter or an empty string
"""

def is_palindrome(word):
    """This function checks if the string is a 
    palindrom or not, then retun a boolean
    
    word: string
    """
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))


