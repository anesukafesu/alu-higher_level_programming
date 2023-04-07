#!/usr/bin/python3
"""
Making an HTTP request using urllib
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        content = response.read()
        print('Body response:')
        print(f'\t- type: {type(content)}')
        print(f'\t- content: {content}')
        print(f'\t- utf8 content: {content.decode("utf-8")}')
