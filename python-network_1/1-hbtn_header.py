#!/usr/bin/python3
"""Getting header values from response"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.get_header('X-Request_Id'))
