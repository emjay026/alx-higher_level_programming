#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_size = len(argv)
    print("{:d} {}{}".format(arg_size - 1,
                             "argument" if arg_size == 2 else "arguments",
                             "." if arg_size == 1 else ":"))
    for i, arg in enumerate(argv[1:], start=1):
        print("{:d}: {}".format(i, arg))
