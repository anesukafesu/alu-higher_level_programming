#!/usr/bin/python3


def max_integer(my_list=[]):

    # Smallest int that can be stored on my system
    # Obviously hardcoding the number is a bad idea
    # But I am not allowed to import any modules
    # This includes the sys module
    max_int = -9223372036854775808

    for num in my_list:
        if num > max_int:
            max_int = num

    return max_int
