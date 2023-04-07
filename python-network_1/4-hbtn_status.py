#!/usr/bin/python3
"""making requests using requests"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    data = response.text

    print('Body response:')
    print('- type: {}'.format(type(data)))
    print('- content: {}'.format(data))
