#!/usr/bin/python3
"""This module contains the matrix_divided function.

The function divides all elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix (list of lists): list of lists of integers/floats.
        div (int/float): divisor.

    Returns:
        list of lists: new matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats.
        TypeError: if rows are not the same size.
        TypeError: if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError(msg)

    if any(row == [] for row in matrix):
        raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
