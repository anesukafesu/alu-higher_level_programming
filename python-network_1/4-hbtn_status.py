#!/usr/bin/python3
import requests
"""making requests using requests"""


if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    data = response.text

    print('Body response:')
    print(f'\t- type: {type(data)}')
    print(f'\t- type: {data}')
