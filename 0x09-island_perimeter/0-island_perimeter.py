#!/usr/bin/python3
""" island_perimeter function """


def island_perimeter(grid):
    """
    Function to calculate the perimeter of an island in a grid.

    Parameters:
    grid (list of list of int): The grid representing the map.
    0 represents water, 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    def edges(matrix):
        count = 0
        for row in matrix:
            row = [0] + row + [0]
            for i in range(1, len(row)):
                count += row[i] != row[i-1]
        return count

    tgrid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, item in enumerate(row):
            tgrid[i].append(item)

    return edges(grid) + edges(tgrid)
