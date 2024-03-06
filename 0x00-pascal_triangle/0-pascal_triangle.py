#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        previous_row = triangle[-1]
        new_row = [previous_row[0]]

        for i in range(1, len(previous_row)):
            new_row.append(previous_row[i - 1] + previous_row[i])

        new_row.append(previous_row[-1])
        triangle.append(new_row)

    return triangle
