#!/usr/bin/python3
"""
Implements the print_square function
"""


def print_square(size):
    """
    prints #s in the shape of a square
    length and width are equal to the size parameter
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    row = ("#" * size) + "\n"
    square = row * size

    print(square, end="")
