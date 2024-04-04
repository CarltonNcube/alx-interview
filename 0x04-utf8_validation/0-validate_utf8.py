#!/usr/bin/env python3

"""
Defines a method to determine a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: list of integers representing 1 byte of data each

    Returns:
    - True if data is a valid UTF-8 encoding, else False
    """
    num_bytes_to_follow = 0
    
    for byte in data:
        byte = bin(byte)[2:].zfill(8)
        
        if num_bytes_to_follow == 0:
            if byte.startswith('0'):
                continue
            elif byte.startswith('110'):
                num_bytes_to_follow = 1
            elif byte.startswith('1110'):
                num_bytes_to_follow = 2
            elif byte.startswith('11110'):
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if not byte.startswith('10'):
                return False
            num_bytes_to_follow -= 1
    
    return num_bytes_to_follow == 0
