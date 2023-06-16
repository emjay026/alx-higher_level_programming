#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) is not str:
        return 0

    sum = 0

    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}

    for i in range(len(roman_string)):
        if i > 0 and rom_int[roman_string[i].upper()] > rom_int[roman_string[i - 1].upper()]:
            sum += rom_int[roman_string[i].upper()] - 2
        else:
            sum += rom_int[roman_string[i].upper()]

    return sum
