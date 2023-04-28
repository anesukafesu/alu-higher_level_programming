#!/usr/bin/python3
"""Implements text_indentation"""


def text_indentation(text):
    """Adds two new lines after '?', '.' and ':'"""
    if not type(text) is not str:
        raise TypeError("text must be a string")

    b = 0
    while b < len(text) and text[b] == ' ':
        b += 1

    while b < len(text):
        print(text[b], end="")
        if text[b] == "\n" or text[b] in ".?:":
            if text[b] in ".?:":
                print("\n")
            b += 1
            while b < len(text) and text[b] == ' ':
                b += 1
            continue
        b += 1
