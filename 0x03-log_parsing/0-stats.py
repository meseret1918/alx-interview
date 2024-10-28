#!/usr/bin/python3
"""
Script that reads from standard input and computes metrics.
"""

import sys

def print_stats(total_size, status_counts):
    """
    Prints the accumulated statistics including total file size and status codes count.
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

total_size = 0
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        # Check if the line has the correct format
        if len(parts) < 7:
            continue

        # Get the status code and file size
        status_code = parts[-2]
        file_size = parts[-1]

        # Check if file size is a digit and add to total size
        if file_size.isdigit():
            total_size += int(file_size)

        # Check if status code is in the allowed list and increment count
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

# Print the final statistics after reading all lines
print_stats(total_size, status_counts)
