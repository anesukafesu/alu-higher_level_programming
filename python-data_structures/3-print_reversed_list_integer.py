#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    
    if my_list != None:
        start = len(my_list) - 1
        end = -1
        step = -1

        for i in range(start, end, step):
            print("{:d}".format(my_list[i]))
