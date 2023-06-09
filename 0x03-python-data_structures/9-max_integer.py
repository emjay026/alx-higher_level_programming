#!/usr/bin/python3
def max_integer(my_list=[]):
    list_size = len(my_list)
    if (list_size == 0):
        return None
    largest = my_list[0]
    for i in range(list_size):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
