# CS362 test_leap_year.py
# Alex Young
# 3/2/2021
# Run this file using python3 test_leap_year.py or just pytest
# This program tests if the Leap Year program works correctly

import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    def test_add(self):
        self.assertEqual(leap_year.run(-1), "is not a leap year")
        self.assertEqual(leap_year.run(0), "is a leap year")
        self.assertEqual(leap_year.run(1), "is not a leap year")
        self.assertEqual(leap_year.run(4), "is a leap year")
        self.assertEqual(leap_year.run(100), "is not a leap year")
        self.assertEqual(leap_year.run(400), "is a leap year")
        self.assertEqual(leap_year.run(401), "is not a leap year")
        self.assertEqual(leap_year.run(2000), "is a leap year")
        self.assertEqual(leap_year.run("0"), "invalid input")


if __name__ == '__main__':
    unittest.main(verbosity=2)