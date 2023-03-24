#!/usr/bin/python3
def magic_string():
    return ("BestSchool, " * ((magic_string.c := magic_string.c + 1) - 1)) + "BestSchool"
magic_string.c = 0
