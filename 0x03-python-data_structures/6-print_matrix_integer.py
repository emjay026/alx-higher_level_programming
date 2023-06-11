#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        inner_len = len(matrix[i])
        for j in range(inner_len):
            print("{:d}{}".format(matrix[i][j], "" if j == inner_len - 1
                                  else " "), end='')
        else:
            print("")
