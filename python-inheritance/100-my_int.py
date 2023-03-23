#!/usr/bin/python3
"""
Implements MyInt class
Classes:
    MyInt
"""


class MyInt(int):
    """
    MyInt class
    Custom int class with unexpected behaviours
    """
    def __eq__(self, other):
        if type(other) == int:
            other = self.__class__(int)

        return self != other

    def __ne__(self, other):
        if type(other) == int:
            other = self.__class__(int)

        return self == other
