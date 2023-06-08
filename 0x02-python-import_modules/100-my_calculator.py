#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    arg_size = len(argv)

    if arg_size != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    for item in ['+', '-', '*', '/']:
        if (argv[2] == item):
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
