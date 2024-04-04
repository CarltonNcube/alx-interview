#!/usr/bin/python3
"""
Defines a method which determine a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0
    msb_mask = 1 << 7
    two_msb_mask = 1 << 6

    for num in data:
        mask = msb_mask

        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & msb_mask and not (num & two_msb_mask)):
                return False

        n_bytes -= 1

    return n_bytes == 0
