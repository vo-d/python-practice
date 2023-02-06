def count_letter(string):
    """This function create a dictionary with key is the 
    letter and value is the number of its appearance

    string: string
    Returns: dictionary
    """
    dict = {}
    for char in string:
        dict.setdefault(char, 0)
        dict[char] += 1
    return dict


def invert_dict(string):
    """This function invert the dictionary created in 
    count_letter() to create a new dictionary with key 
    is the frequency of letter and value is the list of 
    letter with that frequency

    string: string
    Returns: dictionary
    """
    dict = count_letter(string)
    inverse = {}
    for key in dict:
        value = dict[key]
        inverse.setdefault(value, []).append(key)
    return inverse


def most_frequent(string):
    """This function take a string and print out the letters
    in decreasing order of frequency

    string: string
    """
    inverse = invert_dict(string)
    key_list = list(inverse.keys())
    key_list.sort(reverse = True)
    for key in key_list:
        for letter in inverse[key]:
            print(letter)
    

# Test run
if __name__ == '__main__':
    """I use words.txt to test most_frequent method 
    """
    string = open('words.txt').read()
    most_frequent(string)