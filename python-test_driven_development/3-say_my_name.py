#!/usr/bin/python3
"""
Says your name out loud
"""


def say_my_name(first_name, last_name=""):
    """
    Says the provided name in a sentence
    """
    try:
        if type(first_name) is not str:
            raise Exception('first_name')

        if type(last_name) is not str:
            raise Exception('last_name')
    except Exception as e:
        raise TypeError(f'{e} must be a string')

    print(f'My name is {first_name} {last_name}')
