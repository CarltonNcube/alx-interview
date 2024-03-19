#!/usr/bin/python3
"""Defines a method to calculate the fewest operations needed."""


def minOperations(n):
    """
    Calculate the fewest operations for exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: Minimum operations needed, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
