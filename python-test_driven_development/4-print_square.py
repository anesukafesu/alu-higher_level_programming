#!/usr/bin/python3
"""
Implements the print_square function
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    row = ("#" * size) + "\n"
    square = row * size

    print(square, end="")
