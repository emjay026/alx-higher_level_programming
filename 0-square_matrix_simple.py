#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    outer_len = len(matrix)
    for i in range(outer_len):
        row = []
        inner_len = len(matrix[i])
        for j in range(inner_len):
            row.append(matrix[i][j] ** 2)
        new_matrix.append(row)
    return new_matrix
