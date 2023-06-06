#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_number = str(number)
str_last = (str_number[0] + str_number[-1]) if (number < 0) else str_number[-1]
last = int(str_last)

if last > 5:
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number:d} is {last:d} and is 0")
elif last < 6:
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
