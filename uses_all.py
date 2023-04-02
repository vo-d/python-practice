import pandas as pd

def uses_all(word, letters):
    """
    This function takes a word and a string of letters, and that returns True if the 
    word contains only letters in the list.

    word: string
    letter: string
    return: boolean
    """

    word_df = pd.DataFrame(list("".join(word.lower().split())), columns=["char"])
    letters_df = pd.DataFrame(list("".join(letters.lower().split())), columns=["char"]) 
    if(word_df["char"].isin(letters_df["char"]).all() == True):
        return letters_df["char"].isin(word_df["char"]).all()
    else:
        return False

    
print(uses_all("Hoe alfalfac", "acefhlo") == True)

def test_uses_all():
    assert uses_all("Hoe alfalfa", "acefhlo") == False
    assert uses_all("aeiouy", "aeiou") == False
    assert uses_all("Hoe alfalfac", "acefhlo") == True
