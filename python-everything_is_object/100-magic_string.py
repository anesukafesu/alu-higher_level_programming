#!/usr/bin/python3
def magic_string():
    global count
    count += 1
    return ("BestSchool, " * (count - 1)) + "BestSchool"
