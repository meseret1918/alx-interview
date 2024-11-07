#!/usr/bin/python3
'''A script that reads HTTP request logs from stdin and computes metrics.
'''

import sys


def print_metrics(total_size, status_codes):
    '''Print the accumulated metrics.'''
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            # Check if the line matches the expected format
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip lines that don't have enough parts
            
            # Extract relevant information
            try:
                file_size = int(parts[-1])  # Ensure this is an integer
                status_code = parts[-2]
            except (ValueError, IndexError):
                continue  # Skip lines that do not have the expected integer format
            
            # Update the total size and the status codes
            total_size += file_size
            if status_code.isdigit() and int(status_code) in status_codes:
                status_codes[int(status_code)] += 1
            
            line_count += 1
            
            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == '__main__':
    main()