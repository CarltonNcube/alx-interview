#!/usr/bin/python3
"""Function to generate Pascal's Triangle.

This module defines a function `pascal_triangle(n)` that returns
a list of lists of integers representing Pascal's Triangle of n.

Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    result = []
    for line in range(n):
        row = []
        x = 1
        for i in range(line + 1):
            row.append(x)
            b = (i + 1)
            x = x * (line - i) // b
        result.append(row)
    return result
