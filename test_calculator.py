# Repository: https://github.com/LeandroMarulanda/lab10-LeandroMarulanda-MichaelHushebeck
# Partner 1: Leandro Marulanda
# Partner 2: Michael Hushebeck

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    # Michael Hushebeck's tests

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    # Leandro Marulanda's tests

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-10, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)

    def test_negative_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_negative_hypotenuse(self):
        with self.assertRaises(ValueError):
            hypotenuse(-3, 4)

    # Additional tests for remaining functions

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)

    def test_sub(self):
        self.assertEqual(sub(10, 3), 7)

    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_log(self):
        self.assertAlmostEqual(log(100, 10), 2)

    def test_log_invalid(self):
        with self.assertRaises(ValueError):
            log(-10, 10)

    def test_exp(self):
        self.assertEqual(exp(2, 3), 8)


if __name__ == "__main__":
    unittest.main()
