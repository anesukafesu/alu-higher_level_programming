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
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
