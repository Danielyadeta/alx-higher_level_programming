#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = number

lastD = number % 10

if lastD > 5:
    string = "and is greater than 5"
elif lastD == 0:
    string = "and is 0"
elif lastD < 6:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, lastD), string)
