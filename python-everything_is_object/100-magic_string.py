#!/usr/bin/python3
count = 0
def magic_string():
    return ("BestSchool, " * ((count := count + 1) - 1)) + "BestSchool"
