#!/usr/bin/python3
def magic_string():
    global count
    return ("BestSchool, " * ((count := count + 1) - 1)) + "BestSchool"
