#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for i in range(len(str)):
        s = ord(str[i])
        print("{:c}".format(s - 32 if islower(str[i]) else s), end='')
    print('')
