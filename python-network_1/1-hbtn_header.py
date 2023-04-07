#!/usr/bin/python3
"""Getting header values from response"""
import urllib
import sys


if __name__ == "__main__":
    with urllib.request.open(sys.argv[1]) as request:
        print(request.get_header('X-Request_Id'))
