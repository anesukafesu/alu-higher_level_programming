#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if key == "" or key not in dict:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
