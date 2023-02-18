#!/usr/bin/python3
import sys

def main():
    n = len(sys.argv)
    total = 0

    for i in range(1, n):
        total += int(sys.argv[i])

    print(total)


if __name__ == "__main__":
    main()
