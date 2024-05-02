#!/usr/bin/python3
"""Module for makeChange method"""

def makeChange(coins, total):
    """Determine the fewest coins needed to meet a given amount total.
    
    Args:
        coins (list): The values of the coins in your possession
        total (int): The total amount to meet

    Returns:
        int: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
