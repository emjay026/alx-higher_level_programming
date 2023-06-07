#!/usr/bin/python3
def islower(c):
    c_num = ord(c)
    if c_num > 96 and c_num < 123:
        return True
    else:
        return False
