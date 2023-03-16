#!/usr/bin/python3

"""
Another world-changing square module
"""


class Square:
    """
    Here's the good part
    """
    def __init__(self, size=0):
        """
        Size property is optional because size
        does not matter
        """
        self.__size = size

    @property
    def size(self):
        """
        Square v2 now can retrieve properties
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        And you can set them too using
        a fancy concept called polymorphism
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2
