#!/usr/bin/python3
"""Printing Error codes of requests"""
from urllib import error, request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(e.code)
