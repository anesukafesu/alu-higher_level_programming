#!/usr/bin/python3


def magic_calculation(a, b):
    _temp = __import__('magic_calculation_102', ('add', 'sub'), 0)
    add = _temp.add
    sub = _temp.sub

    if b > a:
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c
    else:
        return sub(a, b)
