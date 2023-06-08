#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []
    j = 0
    for i in range(len(str)):
        if i != n:
            new_str.append(str[i])
    return new_str
