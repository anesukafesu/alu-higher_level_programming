#!/usr/bin/python3
def magic_string():
    magic_string.c = 1 if magic_string.c is None else magic_string.c + 1
    return ("BestSchool, " * (magic_string.c - 1)) + "BestSchool"
