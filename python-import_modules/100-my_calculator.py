#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    c = 0

    if op == '+':
        c = add(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '/':
        c = div(a, b)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print("{} {} {} = {}".format(a, op, b, c))


if __name__ == '__main__':
    main()
