#!/usr/bin/python3


def list_division(list_1, list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            new_list.append(list_i[i] / list_2[i])
        except:
            new_list.append(0)

    return new_list
