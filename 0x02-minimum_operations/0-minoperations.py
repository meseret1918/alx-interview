#!/usr/bin/python3
"""
Minimum Operations

This script calculates the fewest number of operations needed
to achieve exactly n 'H' characters in a text file using
only the operations: Copy All and Paste.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations to get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
             Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    current_chars = 1
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor  # Copy and Paste actions
            n //= factor
            current_chars *= factor
        else:
            factor += 1

    return operations

