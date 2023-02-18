#!/usr/bin/python3
import sys


def main():
    number_of_arguments = len(sys.argv) - 1
    print("{}".format(number_of_arguments), end=" ")

    if number_of_arguments == 0:
        print("arguments.")
    elif number_of_arguments == 1:
        print("argument:")
    else:
        print("arguments:")

    for i in range(1, number_of_arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
