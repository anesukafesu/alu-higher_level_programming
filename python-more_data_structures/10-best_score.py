#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_score = -9223372036854775806
    max_key = ""

    for key in a_dictionary:
        if a_dictionary[key] > max_score:
            max_score = a_dictionary[key]
            max_key = key

    return max_key if max_key != "" else None
