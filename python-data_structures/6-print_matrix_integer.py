#!/usr/bin/python3


def print_matrix_integer(matrix=[]):
    for row in matrix:
        row_output = ""

        for i in range(len(row)):
            row_output += "{:d}".format(row[i])

            if i != len(row) - 1:
                row_output += " "

        print(row_output)
