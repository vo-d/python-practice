import math


def is_square(number : float) -> bool:
    """
    return a boolean on if input number is square or not
    assert means if the condition is true, then move on, if false, then fail
    """
    assert number >= 0, 'expect a non-negative number'

    try: 
        root = math.sqrt(number)
    except ValueError as exc:
        print(exc)
    return root == int(root)


def test_is_square():
    print('Testing with 5') # pytest -s will show this even if test passes
    assert not is_square(5)
    
    print('Testing with 4')
    assert  is_square(4)
    assert not is_square(-4)
    
if __name__ == '__main__':
    number = float(input('Enter a number: '))
    if is_square(number):
        print('It is square')
    else:
        print('It is not square')
