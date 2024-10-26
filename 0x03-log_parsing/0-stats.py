#!/usr/bin/python3
"""
Log Parsing Script

This script reads HTTP request logs from stdin and computes metrics.
It prints the total file size and counts of each HTTP status code
after every 10 lines and upon script termination (via KeyboardInterrupt).
"""

import sys
import re


def output(log):
    """
    Helper function to display the accumulated log statistics.
    Prints the total file size and the frequency of each HTTP status code.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    # Regular expression pattern to match the log format.
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
        r'\d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" '
        r'(\d{3}) (\d+)'  # Matches the HTTP status code and file size
    )

    # Initialize counters and storage for log data.
    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # Update total file size
                log["file_size"] += file_size

                # Update status code frequency if it's a tracked code
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        # On manual interruption, print statistics and exit
        output(log)
        raise
    finally:
        # Ensure final output regardless of how the script exits
        output(log)
