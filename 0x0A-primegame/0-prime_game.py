#!/usr/bin/python3
"""
Prime Game module.

This module implements the logic for determining the winner of the Prime Game.
"""

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers, where each integer represents the range of numbers for the game.

    Returns:
        str: Name of the winner ("Maria" or "Ben"), or None if there is no winner.
    """
    if x <= 0 or not nums or any(n < 1 for n in nums):
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[:n + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

def sieve_of_eratosthenes(n):
    """
    Generate a list of prime indicators up to n using Sieve of Eratosthenes.

    Args:
        n (int): The upper limit to calculate primes.

    Returns:
        list: A list where primes[i] is True if i is a prime number, otherwise False.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

if __name__ == "__main__":
    # Example test cases
    print(isWinner(3, [4, 5, 1]))  # Expected: "Ben"
