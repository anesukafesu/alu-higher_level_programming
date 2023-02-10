#!/usr/bin/python3


def print_last_digit(number):
    if isinstance(number, int):
        last_digit = str(number)[-1]
        print(last_digit, end="")
        return last_digit
    else:
        raise Exception("Oops")
