import pandas as pd

def has_no_e(file):
    """
    This function read the file and print out all the word that has no letter e
    """
    # Read in the words.txt file as a list of strings
    with open(file, 'r') as f:
        words = f.read().split()

    # Convert the list of strings to a pandas Series
    words_series = pd.Series(words)

    # Count the number of occurrences of "e" in each word
    e_counts = words_series.str.count('e')

    # Filter the Series to include only words without "e"
    no_e_words = words_series[e_counts == 0]

    # Calculate the percentage of words without "e"
    percentage = len(no_e_words) / len(words_series) * 100

    # Print out the results
    print("Words without 'e':")
    print('\n'.join(no_e_words.tolist()))
    print(f"\nPercentage of words without 'e': {percentage:.2f}%")

has_no_e('words.txt')