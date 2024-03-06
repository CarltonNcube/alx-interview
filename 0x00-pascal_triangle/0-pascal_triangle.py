#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row containing only 1
    triangle = [[1]]

    # Generate subsequent rows of Pascal's triangle
    for _ in range(1, n):
        previous_row = triangle[-1]  # Get the previous row
        new_row = [1]  # First element of each row is always 1

        # Iterate over the previous row to calculate values for the new row
        for i in range(1, len(previous_row)):
            new_value = previous_row[i - 1] + previous_row[i]
            new_row.append(new_value)

        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

