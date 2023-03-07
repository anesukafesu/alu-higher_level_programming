#!/usr/bin/python3


def square_array(array):
    return list(map(lambda x: x ** 2, array))


def square_matrix_simple(matrix=[]):
    return list(map(square_array, matrix))
