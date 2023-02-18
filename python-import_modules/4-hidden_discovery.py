#!/usr/bin/python3
from inspect import getmembers, isfunction
import hidden_4


def main():
    members = getmembers(hidden_4, isfunction)

    for member in members:
        name = member[0]

        # Not printing the name if it starts with an underscore
        if name[0] == '_':
            continue

        print(name)


if __name__ == '__main__':
    main()
