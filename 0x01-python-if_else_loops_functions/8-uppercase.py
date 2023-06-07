#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for i in range(len(str)):
        if islower(str[i]):
            s = ord(str[i]) - 32
            print("{:c}".format(s), end='')
        else:
            print(str[i], end='')
    print('')
