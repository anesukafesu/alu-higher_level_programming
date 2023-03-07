#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    to_be_deleted = []

    for key in a_dictionary:
        if a_dictionary[key] == value:
            to_be_deleted.append(key)

    for key in to_be_deleted:
        del a_dictionary[key]

    return a_dictionary
