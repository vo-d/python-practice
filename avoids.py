import pandas as pd

def avoids(word, forbidden_letters):
    """
    This function takes word and forbidden_letters then check if word contains
    any letter in forbidden_letter then return boolean acording to it
    
    word: string
    forbiddent_letter: string
    return: boolean
    """
    word_series = pd.Series(list(word))
    forbidden_series = pd.Series(list(forbidden_letters))

    # Check if any letter in forbidden_letters appears in the word
    has_forbidden_letters = word_series.isin(forbidden_series).any()

    # Return True if the word doesn't contain any forbidden letters
    return not has_forbidden_letters

def test_avoids():
    assert avoids("word", "o") == False
    assert avoids("word", "a") == True


