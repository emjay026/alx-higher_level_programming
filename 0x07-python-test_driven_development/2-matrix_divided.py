#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list or len(matrix) < 1:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_o_mtx = []
    i_mtx_size = len(matrix[0])

    for i_mtx in matrix:
        if len(i_mtx) != i_mtx_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_i_mtx = []
        for n in i_mtx:
            if type(n) not in [int, float]:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_i_mtx.append(round(n / div, 2))
        new_o_mtx.append(new_i_mtx)

    return new_o_mtx
