#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    
    # Clean up tuple a to prevent possible errors
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)

    # Clean up tuple b to prevent possible errors
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_b[0] + tuple_b[0]

    return (first_element, second_element)
