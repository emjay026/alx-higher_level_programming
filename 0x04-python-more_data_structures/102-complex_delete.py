#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    for i in range(len(values)):
        if value == values[i]:
            del a_dictionary[keys[i]]
    return a_dictionary
