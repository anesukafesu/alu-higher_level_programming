#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
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
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, bb, c)
    
    
if __name__ == "__main__":
    main()
