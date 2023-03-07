#!/usr/bin/bash


def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except:
            pass
    
    print()
    return i
