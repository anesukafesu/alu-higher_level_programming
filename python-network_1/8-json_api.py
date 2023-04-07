#!/usr/bin/python3
"""Searching for a user at an API"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        user = ""
    
    response = requests.get(url, params={'q': user})

    if len(response.content) == 0:
        print("No result")
    else:
        try:
            print(response.content)
            json_response = response.json()
            print(json_response)
            print('[{}] {}'.format(json_response.get('id'), json_response.get('name')))
        except:
            print("Not a valid JSON")