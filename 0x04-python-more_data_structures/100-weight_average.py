#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_of_mul = 0
    sum_of_b = 0
    for a, b in my_list:
        sum_of_mul += (a * b)
        sum_of_b += b
    return (sum_of_mul / sum_of_b)
