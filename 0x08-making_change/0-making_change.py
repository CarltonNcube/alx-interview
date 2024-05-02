#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Initialize dp array with total+1 (an impossible value)"""
    dp = [total + 1] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return -1 if dp[total] > total else dp[total]
