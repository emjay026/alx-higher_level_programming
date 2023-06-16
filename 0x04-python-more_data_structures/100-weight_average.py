#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_of_mul = 0
    sum_of_b = 0
    result = 0
    if my_list:
        for a, b in my_list:
            sum_of_mul += (a * b)
            sum_of_b += b
        result = sum_of_mul / sum_of_b
    return (result)
