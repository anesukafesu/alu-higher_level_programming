#!/usr/bin/python3
import functools as f
print(f.reduce(lambda s, c: s+c, map(lambda c: chr(c), range(65, 91))))
