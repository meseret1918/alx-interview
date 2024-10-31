#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for byte in data:
        # Get the first 8 bits of the byte
        byte = byte & 0xFF  # Keep only the last 8 bits

        if num_bytes == 0:  # We are expecting a new character
            if (byte >> 7) == 0b0:
                num_bytes = 0  # 1-byte character
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid start byte
        else:  # We are continuing to read a multi-byte character
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1  # Expect one less byte in the sequence

    return num_bytes == 0  # Ensure all bytes were valid
