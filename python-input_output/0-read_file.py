#!/usr/bin/python3
"""
implements a read_file
Functions:
    - read_file
"""


def read_file(file_name=""):
    with open(file_name) as f:
        content = f.read()
        print(content)
