#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for key in sorted(list(a_dictionary)):
        print(key, end=": ")
        print(a_dictionary[key])
