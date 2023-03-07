#!/usr/bin/python3


def roman_to_int(roman_string):
    # Getting rid of empty strings and invalid data types
    if not isinstance(roman_string, str) or roman_string == '':
        return 0

    # From this point, we can assume the string has at least one char
    mappings = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    last_index = len(roman_string) - 1

    for i in range(last_index + 1):
        curr_val = mappings[roman_string[i]]

        if i < last_index:
            next_val = mappings[roman_string[i + 1]]

            if curr_val < next_val:
                total -= curr_val
            else:
                total += curr_val
        else:
            total += curr_val

    return total

roman_to_int('XXVIII')
