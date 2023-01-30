def rotate_letter(letter, i):
    """This function rotates a word by i places. 
    Does not change other chars.

    letter: string
    i: integer
    Returns: string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    a = ord(letter) - start
    b = (a + i) % 26 + start
    return chr(b)


def rotate_word(word, i):
    """This function rotates a word by i places.

    word: string
    i: integer
    Returns: string
    """
    new_string = ''
    for letter in word:
        new_string += rotate_letter(letter, i)
    return new_string


