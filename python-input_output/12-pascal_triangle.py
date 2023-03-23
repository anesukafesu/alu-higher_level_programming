#!/usr/bin/python3
"""
Implements Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns an array of rows of pascals triangle
    Each row is a list of integers in that row
    """
    if n == 0:
        return []

    rows = [[1]]

    for row_count in range(2, n + 1):
        if row_count == 2:
            rows.append([1, 1])
        else:
            row = [1]
            for i in range(1, row_count - 1):
                row.append(rows[-1][i - 1] + rows[-1][i])

            row.append(1)
            rows.append(row)

    return rows
