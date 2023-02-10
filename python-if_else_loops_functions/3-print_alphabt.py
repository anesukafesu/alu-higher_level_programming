#!/usr/bin/python3
# comment maybe?

for i in range(97, 123):
    # Checking for e and q
    if not (i == 101 or i == 113):
        print("{:s}".format(chr(i)), end="")
