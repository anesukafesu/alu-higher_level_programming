#!/usr/bin/python3
import functools
print(functools.reduce(lambda str_so_far, char: str_so_far + char, map(lambda c: chr(c), range(65, 91))))
