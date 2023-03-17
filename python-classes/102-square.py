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
        self.size = size

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, s):
        return self.size == s.size

    def __lt__(self, s):
        return self.size < s.size

    def __gt__(self, s):
        return self.size > s.size

    def __le__(self, s):
        return self.size <= s.size

    def __ge__(self, s):
        return self.size >= s.size

    def __ne__(self, s):
        return self.size != s.size
