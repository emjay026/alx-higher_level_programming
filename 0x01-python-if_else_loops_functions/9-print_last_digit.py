#!/usr/bin/python3
def print_last_digit(number):
    n = (number * -1) % 10 if number < 0 else number % 10
    print(f"{n:d}", end='')
    return n
