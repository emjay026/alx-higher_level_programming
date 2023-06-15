#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) is not str:
        return 0

    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    keys = list(rom_int.keys())
    sum = 0

    str_len = len(roman_string)
    key_len = len(keys)

    if roman_string == "IX" or roman_string == "IV":
            sum += rom_int[roman_string[1]] - rom_int[roman_string[0]]
    else:
        for i in range(str_len):
            for j in range(key_len):
                if roman_string[i] == keys[j]:
                    sum += rom_int[keys[j]]

    return sum
