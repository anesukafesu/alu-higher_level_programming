#!/usr/bin/python3


def best_score(a_dictionary):
    max_score = -9223372036854775806

    for key in a_dictionary:
        if a_dictionary[key] > max_score:
            return key

    return None
