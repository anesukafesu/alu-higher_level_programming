#!/usr/bin/python3


"""
This module demonstrates how to create classes
that can be initialised and store private fields
"""

class Square:
    """
    This class takes creates a square
    """

    def __init__(self, size):
        """
        Pass in the size of the square
        """
        self.__size = size
