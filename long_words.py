import pandas as pd

def long_words(file):
    """
    This function read the file and print out all the word that is longer than 
    20 characters
    """
    df = pd.read_csv(file, header=None, names=['words'])
    df['characters'] = df['words'].str.split('')
    df['num_characters'] = df['characters'].str.len()

    # use mask to get filter result
    long_words = df[df['num_characters'] > 20]

    print(long_words['words'])

long_words('words.txt')