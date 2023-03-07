#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    output = []

    for num in my_list:
        output.append(num % 2 == 0)

    return output
