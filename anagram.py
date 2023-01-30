def is_anagram(str1, str2):
    """This function check if two string are 
    anagrams

    str1: string or array
    str2: string or array
    returns: boolean
    """
    return sorted(str1) == sorted(str2)