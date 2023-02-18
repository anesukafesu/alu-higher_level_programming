#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    # Can't think of a more elegant way to do it
    display(a, b, add(a, b), '+')
    display(a, b, sub(a, b), '-')
    display(a, b, mul(a, b), '*')
    display(a, b, div(a, b), '/')


def display(a, b, c, sign):
    print("{} {} {} = {}".format(a, sign, b, c))


if __name__ == "__main__":
    main()
