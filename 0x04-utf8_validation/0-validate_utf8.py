#!/usr/bin/python3
"""UTF-8 Validation"""

def get_leading_set_bits(num):
    """Returns the number of leading set bits (1)."""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper >>= 1  # Shift right
    return set_bits


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            leading_bits = get_leading_set_bits(byte)
            # If it's a single-byte character
            if leading_bits == 0:
                continue
            # Valid number of leading bits (1 to 4)
            if leading_bits == 1 or leading_bits > 4:
                return False
            remaining_bytes = leading_bits - 1  # Set remaining bytes
        else:
            # Check for continuation byte (10xxxxxx)
            if not (byte & 0b10000000) or (byte & 0b11000000) != 0b10000000:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0  # True if all bytes are valid
