#!/usr/bin/python3
import urllib.request


with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    print(response.read())
