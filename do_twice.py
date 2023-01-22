def do_twice(function, arg):
    function(arg)
    function(arg)


def print_twice(arg):
    print(arg, end=" ")
    print(arg)
    

def do_four(function, arg):
    do_twice(function, arg)
    do_twice(function, arg)


do_twice(print, "spam")
print('')
do_four(print, 'spam')
print_twice("spam")