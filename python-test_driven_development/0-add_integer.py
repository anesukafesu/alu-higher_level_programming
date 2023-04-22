#!/usr/bin/python3
"""
Implement the add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b
    Ensures they are integers, else exceptions will be raised
    If they are floats, they are first converted
    The result is returned as an int
    """

    # Checks if an argument is valid
    # Returns the argument converted to an int
    def ensure_is_valid(name, value):
        value_type = type(value)

        if value_type is not int and value_type is not float:
            raise TypeError(f'{name} must be an integer')

        return int(value)

    a = ensure_is_valid('a', a)
    b = ensure_is_valid('b', b)

    return a + b
