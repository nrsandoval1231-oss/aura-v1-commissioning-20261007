import unittest

from greeting import greet, multiply


class GreetingTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greet("Ada"), "Hi, Ada.")

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_and_positive_numbers(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 9), 0)


if __name__ == "__main__":
    unittest.main()
