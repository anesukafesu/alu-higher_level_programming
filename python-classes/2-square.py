#!/usr/bin/python3
"""
This module also demonstrates creating Python classes
Using the constructor method and validating arguments
"""


class Square:
    """
    This square validates data
    """

    def __init__(self, size=0):
        """
        The constructor takes in a size int as an arg
        If size < 0 a ValueError exception will be raised
        If size is not an int a TypeError exception will be raised
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
