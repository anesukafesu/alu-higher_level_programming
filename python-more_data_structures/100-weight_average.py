#!/usr/bin/python3


def weight_average(my_list=[]):
    item_count = 0
    total = 0

    for record in my_list:
        total += record(0) * record(1)
        item_count += record(1)
    
    return 0 if item_count == 0 else total / item_count
