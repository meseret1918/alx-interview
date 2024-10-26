#!/usr/bin/python3
'''A script that generates random HTTP request logs.
This script simulates HTTP GET requests with random IP addresses,
timestamps, and status codes.
'''

import random
import sys
import datetime
from time import sleep


def generate_log_entry():
    '''Generates a single log entry in the HTTP request log format.'''
    ip = "{:d}.{:d}.{:d}.{:d}".format(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255)
    )
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    response_size = random.randint(1, 1024)

    log_entry = (
        f"{ip} - [{timestamp}] \"GET /projects/1216 HTTP/1.1\" "
        f"{status_code} {response_size}\n"
    )
    return log_entry


def main():
    '''Main function to generate 10,000 log entries.'''
    for _ in range(10000):
        sleep(random.uniform(0, 0.1))  # Limit maximum delay to 100 ms
        sys.stdout.write(generate_log_entry())
        sys.stdout.flush()


if __name__ == '__main__':
    main()
