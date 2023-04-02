import pandas as pd

def forbidden_2(file):
    """
    This function take a file then ask user for input. After that, it will
    return all of the word in the file that don't contain any letter in 
    forbidden_letter

    file: string
    """
    words = pd.read_csv(file , header=None)[0].tolist()
    forbidden_letters = input("Enter a string of forbidden letters: ")

    # create a boolean mask indicating which words contain any forbidden letters
    mask = pd.Series(words).str.contains(f"[{forbidden_letters}]")

    num_valid_words = len(words) - mask.sum()
    print(f"There are {num_valid_words} valid words.")


forbidden_2('words.txt')