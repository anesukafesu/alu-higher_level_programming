#!/usr/bin/python3


def magic_calculation(a, b, c):
    if not b < a:
        if not c > b:
            return a * b - c
        else:
            return a + b
    else:
        return c
