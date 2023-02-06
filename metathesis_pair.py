def difference_amount(word1, word2):
    """This function return the number of differences between 
    two words.

    word1, word2: string
    Returns: integer
    """
    # stop the comparing two words have different length
    assert len(word1) == len(word2)
    
    words_zip = zip(word1, word2)
    count = 0
    for c1, c2 in words_zip:
        if c1 != c2:
            count += 1

    return count


def metathesis_pairs(dictionary):
    """This function get a dictionary of anagram and then find 
    all metathesis pairs

    dictionary: dictionary
    """
    for word1 in dictionary.values():
        for word2 in dictionary.values():
            # word1 < word2 since we don't want to compare the same 
            # pairs again
            if word1 < word2 and difference_amount(word1, word2) == 2:
                print(word1, word2)


