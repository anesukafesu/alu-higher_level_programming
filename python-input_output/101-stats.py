#!/usr/bin/python3
"""
script to parse and collect stats on web server logs
"""

import sys
import signal


def main():
    status_codes_frequency = {}
    total_file_size = 0
    count = 0
    
    # Summarises the values and resets them
    def summarise_and_reset():
        nonlocal status_codes_frequency
        nonlocal total_file_size

        # Print the file size
        print("File size:", total_file_size)

        # Print status codes
        for status_code in status_codes_frequency:
            print(f'{status_code} : {status_codes_frequency[status_code]}')

        # Reset file size
        total_file_size = 0
        # Reset status codes
        status_codes_frequency = {}

    # Summarise and reset on SIGINT signal
    signal.signal(signal.SIGINT, summarise_and_reset)
    
    # Loops each line in stdin 
    for line in sys.stdin:
        # parse line to extract info
        fields = line.strip().split()
        status_code = fields[-2]
        file_size = int(fields[-1])

        # Add status_code to our hash
        if status_code in status_codes_frequency:
            status_codes_frequency[status_code] += 1
        else:
            status_codes_frequency[status_code] = 1

        # increase total_file_size
        total_file_size += file_size

        # increment count
        count += 1

        # check if we should summarise
        if count % 10 == 0:
            summarise_and_reset()
    
    # If we run out lines before a sigint or get a multiple of 10
    # We just summarise what we currently have
    summarise_and_reset()

if __name__ == "__main__":
    main()
