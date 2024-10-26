#!/usr/bin/python3
import sys


def main():
    total_size = 0
    status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            # Parse the line
            parts = line.split()
            if len(parts) < 7:
                continue  # skip invalid lines

            # Extract the file size and status code
            try:
                status_code = int(parts[6])
                file_size = int(parts[7])
            except (ValueError, IndexError):
                continue  # skip lines that do not conform to the format

            # Update metrics
            total_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes_count)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes_count)


def print_stats(total_size, status_codes_count):
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        count = status_codes_count[code]
        if count > 0:
            print(f"{code}: {count}")


if __name__ == "__main__":
    main()
