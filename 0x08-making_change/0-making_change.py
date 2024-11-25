#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The target amount.
    
    Returns:
        int: Fewest number of coins needed to meet total or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through each coin and update dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means total can't be made
    return dp[total] if dp[total] != float('inf') else -1
