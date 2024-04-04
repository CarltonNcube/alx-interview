#!/usr/bin/python3

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: list of integers representing 1 byte of data each

    Returns:
    - True if data is a valid UTF-8 encoding, else False
    """
    # Helper function to count leading set bits
    def count_leading_set_bits(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count
    
    num_bytes_to_follow = 0
    
    for byte in data:
        if num_bytes_to_follow == 0:
            leading_bits = count_leading_set_bits(byte)
            if leading_bits == 0:
                continue
            if leading_bits == 1 or leading_bits > 4:
                return False
            num_bytes_to_follow = leading_bits - 1
        else:
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
            num_bytes_to_follow -= 1
    
    return num_bytes_to_follow == 0
