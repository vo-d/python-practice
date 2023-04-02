import pandas as pd

def uses_only(word, letters):
    """
    This function takes a word and a string of letters, and that returns True if the 
    word contains only letters in the list.

    word: string
    letter: string
    return: boolean
    """
    word_df = pd.DataFrame(list("".join(word.lower().split())), columns=["char"])
    letters_df = pd.DataFrame(list("".join(letters.lower().split())), columns=["char"])

    # check if all the characters in the word are in the letters
    return word_df["char"].isin(letters_df["char"]).all()

def test_use_only():
    assert uses_only("Hoe alfalfa", "acefhlo") == True
    assert uses_only("Hi", "acefhlo") == False

