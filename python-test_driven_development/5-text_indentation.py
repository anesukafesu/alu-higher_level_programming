#!/usr/bin/python3
"""
Implements the text_indentation method
"""


def text_indentation(text):
    """
    indent text? insert new lines in weird places
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    if text == '':
        return

    special_chars = ':,?'

    for special_char in special_chars:
        text = text.replace(special_char, f'{special_char}\n\n')

    lines = text.split('\n')

    for line in lines:
        print(line.lstrip().rstrip())
