#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new_list = []
        for i in range(len(my_list)):
            if idx == i:
                new_list.append(element)
            else:
                new_list.append(my_list[i])
        return new_list
