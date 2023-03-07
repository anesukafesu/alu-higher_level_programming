#!/usr/bin/python3

def square_array(array):
    return map(lambda x: x ** 2, array)


def square_matrix_simple(matrix=[]):
    return map(square_array, matrix):
