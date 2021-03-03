# CS362 test_FizzBuzz.py
# Alex Young
# 3/2/2021
# Run this file using python3 test_FizzBuzz.py or just pytest
# This program tests if the FizzBuzz program works correctly

import unittest
import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_add(self):
        self.assertEqual(FizzBuzz.run(0), "Out of Bounds")
        self.assertEqual(FizzBuzz.run(1), 1)
        self.assertEqual(FizzBuzz.run(98), 98)
        self.assertEqual(FizzBuzz.run(100), "Buzz")
        self.assertEqual(FizzBuzz.run(101), "Out of Bounds")
        self.assertEqual(FizzBuzz.run(3), "Fizz")
        self.assertEqual(FizzBuzz.run(5), "Buzz")
        self.assertEqual(FizzBuzz.run(15), "FizzBuzz")
        self.assertEqual(FizzBuzz.run("10"), "Type Error")


if __name__ == '__main__':
    unittest.main(verbosity=2)