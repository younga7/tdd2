# CS362 HW 7
# Alex Young
# 3/2/2021
# Run this file using python3 leap_year.py
# This program finds if a year is a leap year

def run(x):
    try:
        if (x % 4 == 0):
            if (x % 400 == 0):
                return "is a leap year"
            else:
                if (x % 100 == 0):
                    return "is not a leap year"
                else:
                    return "is a leap year"
        else:
            return "is not a leap year"
    except TypeError:
        return("invalid input")