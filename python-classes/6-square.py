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
        Not the most elegant code I have written but hey it works
        """
        error_text = "position must be a tuple of 2 positive integers"
        # Check if it is a tuple
        if isinstance(position, tuple):

            # Check if it is of length 2
            if len(position) == 2:

                # Check if the values are both ints
                if isinstance(position[0], int) and isinstance(position[1], int):
                    # Check if values are both > 0
                    if position[0] >= 0 and position[1] >= 0:

                        self.__position = position
                    else:
                        raise TypeError(error_text)
                else:
                    raise TypeError(error_text)
            else:
                raise TypeError(error_text)
        else:
            raise TypeError(error_text)

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
