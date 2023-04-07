#!/usr/bin/python3
"""Make a request and get a header from the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_header_value = response.headers.get('X-Request-Id')
    print(request_header_value)
