import random


def has_duplicates(list):
    """This function check if in the list, there is any 
    duplicated value

    list: list
    returns: boolean
    """
    # make a copy of t to avoid modifying the list
    list_copy = list[:]
    list_copy.sort()

    # check for adjacent elements that are equal
    for i in range(len(list_copy)-1):
        if list_copy[i] == list_copy[i+1]:
            return True
    return False


def random_birthdays(n):
    """This function return a list of random integer from 
    1 to 365

    n: integer
    returns: list of integers
    """
    list = []
    for i in range(n):
        randomInt = random.randint(1, 365)
        list.append(randomInt)
    return list


def probability(num_students, num_simulations):
    """This function return the probability that two or more
    in 23 student can have the same birthday

    num_students: how many students in the group
    num_simulations: the amount of simulation
    """
    count = 0
    for i in range(num_simulations):
        t = random_birthdays(num_students)
        if has_duplicates(t):
            count += 1
    chance = (count / num_simulations) * 100
    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('the probability of having a duplication is ' + 
           str(chance) + '%')


#Test run
probability(23, 1000)

