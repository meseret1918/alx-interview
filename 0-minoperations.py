#!/usr/bin/python3

"""
    Determine the minimum operations for a given character count.
"""


def minOperations(n):
    """
     Function that calculates fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: characters of numbers to be displayed
        return:
               min number of  operations

    """

    init = 1
    prompt = 0
    counter = 0
    while init < n:
        remainder = n - init
        if (remainder % init == 0):
            prompt = init
            init += prompt
            counter += 2
        else:
            init += prompt
            counter += 1
    return counter
