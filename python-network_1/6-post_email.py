#!/usr/bin/python3
"""Sending request params"""
import requests
import sys


if __name__ == "__main__":
    url = sys.arg[1]
    email = sys.arg[2]

    response = requests.post(url, data: {'email': email})

    print(response.text)
