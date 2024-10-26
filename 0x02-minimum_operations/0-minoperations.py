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
    factor = 2  # Start checking for factors from 2

    # Loop through to find the factors
    while n > 1:
        if n % factor == 0:  # If factor divides n
            operations += factor  # Count Copy and Paste actions
            n //= factor  # Reduce n by the factor
        else:
            factor += 1  # Check the next factor

    return operations  # Return the total number of operations
