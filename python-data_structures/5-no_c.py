#!/usr/bin/python3


def no_c(my_string):
    
    output = ""

    for char in my_string:
        if char is not 'c' and char is not 'C':
            output += char


    return output
