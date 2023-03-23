#!/usr/bin/python3
"""
Implements MyInt class
Classes:
    MyInt
"""

class MyInt(int):
    def __eq__(self, other):
        return self != other

    def __ne__(self, other):
        return self == other
