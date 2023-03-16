#!/usr/bin/python3

"""
This module implements the square class
What's special about this square is that it can
calculate its own area using our special
proprietary algorithm that has been patented
"""


class Square:
    """
    This patented square class
    """
    def __init__(self, size=0):
        """
        Takes in size and ensures it is the right
        data type and is in the right range
        """
        # Check if size is not an int
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        # Check if size is negative
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Our proprietary area calculation algorithm
        It is top secret
        """
        return self.__size ** 2
