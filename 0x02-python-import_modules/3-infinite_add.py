#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_size = len(argv)
    total = 0
    for i in range(1, arg_size):
        total += int(argv[i])
    print("{:d}".format(total))
