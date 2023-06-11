#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            if matrix[i]:
                for j in range(len(matrix[i])):
                    print("{:d}".format(matrix[i][j]), end='')
                else:
                    print('')
