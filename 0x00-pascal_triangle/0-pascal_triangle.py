#!/usr/bin/env python3

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row containing only 1

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element of each row is always 1

        # Calculate the middle elements of the row
        for j in range(1, i):
            new_element = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)

        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)

    return triangle
