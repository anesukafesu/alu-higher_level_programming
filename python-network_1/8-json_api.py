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

    response = requests.post(url, data={'q': user})

    try:
        # JSON response
        json_response = response.json()

        try:
            user_id = json_response['id']
            user_name = json_response['name']
            print('[{}] {}'.format(user_id, user_name))
        except:
            print("No result")
    except:
        print("Not a valid JSON")
