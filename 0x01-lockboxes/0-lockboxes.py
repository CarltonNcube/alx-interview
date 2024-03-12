#!/usr/bin/python3
"""
Module for lockboxes task.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents a box
                      and contains integers as keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set([0])
    for key in keys:
        for box_key in boxes[key]:
            if box_key < len(boxes) and box_key not in keys:
                keys.add(box_key)

    return len(keys) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
