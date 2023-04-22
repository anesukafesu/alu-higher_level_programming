#!/usr/bin/python3
"""
Implements the matrix_divided method
Also includes a few helper methods
"""


def ensure_is_a_matrix(matrix):
    try:
        # Check if matrix is a list
        if type(matrix) is not list:
            raise Exception()

        # Check if each row is a list
        for row in matrix:
            if type(row) is not list:
                raise Exception()

            # Check if each element in the row is a list
            for element in row:
                if type(element) is not float and type(element) is not int:
                    raise Exception()

    except:
        s = 'matrix must be a matrix (list of lists) of integers/floats'
        raise TypeError(s)


def ensure_same_size_rows(matrix):
    size_of_first_row = len(matrix[0])

    for row in matrix:
        if len(row) != size_of_first_row:
            raise TypeError('Each row of the matrix must have the same size')


def ensure_div_is_valid_divisor(div):
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')


def matrix_deepcopy(matrix):
    new_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            new_row.append(element)

        new_matrix.append(new_row)

    return new_matrix


def matrix_divided(matrix, div):
    """
    Performs element-wise division of a matrix by div
    """

    # Perform checks
    ensure_is_a_matrix(matrix)
    ensure_same_size_rows(matrix)
    ensure_div_is_valid_divisor(div)

    # Deep copy matrix
    new_matrix = matrix_deepcopy(matrix)

    n_rows = len(new_matrix)
    n_cols = len(new_matrix[0])

    # Divide and round off to two decimal places
    for i in range(n_rows):
        for j in range(n_cols):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

    # Return a new matrix
    return new_matrix
