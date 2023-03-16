#!/usr/bin/python3

"""
Another world-changing square module
"""


class Square:
    """
    Here's the good part
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Size property is optional because size
        does not matter
        """
        self.__size = size
        self.__add_position(position)

    @property
    def position(self):
        return self.__position

    def __add_position(self, position):
        """
        Private method to validate the position
        """
        if isinstance(position, tuple) and len(position) == 2 and position[0] > 0 and position[1] > 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @position.setter
    def position(self, position):
        self.__add_position(position)

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

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
