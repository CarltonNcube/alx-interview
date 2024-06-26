#!/usr/bin/python3
"""Module for make Change"""


def makeChange(coins, total):
    """Determine fewest coins needed to meet a given amount.

    Args:
        coins (list): Values of the coins in your possession
        total (int): Total amount to meet

    Returns:
        int: Fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
