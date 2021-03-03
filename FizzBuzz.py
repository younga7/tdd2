# CS362 HW 7
# Alex Young
# 3/2/2021
# Run this file using python3 FizzBuzz.py
# This program prints numbers from 1 to 100 with
# multiples of 3 printing "Fizz", multiples of 5
# printing "Buzz" and multiples of both "FizzBuzz"

def run(x):
    try:
        if (x < 1 or x > 100):
            return("Out of Bounds")
    except TypeError:
        return("Type Error")
    if (x % 3 == 0 and x % 5 == 0):
        return "FizzBuzz"
    elif (x % 3 == 0):
        return "Fizz"
    elif (x % 5 == 0):
        return "Buzz"
    else:
        return x

def printFizzBuzz():
    for x in range(100):
        print(run(x + 1))

printFizzBuzz()