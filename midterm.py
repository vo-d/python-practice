""" base_7 = '12345'
base_10 = int(base_7, 7)
print(base_10) """


""" print(r'Spam\n') """

""" def spam():
    print(1+1)

print(callable(spam)) """




""" s = 'my name is Donald Ervin Knuth'

fullname = s.split()
first, middle, last = fullname[3], fullname[4], fullname[5]

assert first == 'Donald'

assert middle == 'Ervin'

assert last == 'Knuth' """


""" temp = 'cold' if 1<10 else 'warm' """





# def order_by_chars(text: str, chars='aeiouy'):
#     """
#     Split the text on whitespace into words and return a string with
#     the words re-ordered in order of the highest proportion of the
#     parameter chars in each word.
#     """
#     # Your code goes here.
#     def char_propotion(word):
#         """
#         This helper function will return the proportion between sum 
#         of the character in word, that appear in chars, and the length
#         of that word

#         word: string
#         """
#         sum = 0
#         for char in word:
#             if char in chars:
#                 sum += 1
#         return sum / len(word)

#     words = text.split()

#     words.sort(key=char_propotion, reverse=True)
#     return ' '.join(words)

#     # Here's one test case to demonstrate:
#     # order_by_chars('a brave new world') should return
#     # 'a brave new world' because:
#     # a is 100% chars
#     # brave is 2/5
#     # new is 1/3
#     # world is 1/5
#     # and 1 > 2/5 > 1/3 > 1/5


# print(order_by_chars('a world new brave'))



def split_increasing_runs(sequence):
    """
    Iterate through the element in the sequence passed in and yield
    runs of those elements as tuples that are equal or increasing (<=).
    """
    pass  # Your code goes here.
    run = [sequence[0]]
    for digit in sequence:
        if digit <= run[-1]:
            yield tuple(run)
            run = []
        run.append(digit)
    yield tuple(run)

    # For example, given [1, 2, 2, 4, 3, 8] the function would return the
    # tuples (1, 2, 2, 4) and (3, 8).