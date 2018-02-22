import unittest
from fib.fibonacci import Fibonacci


class test_fibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def test_min(self):
        self.assertEqual(self.fib.fibonacci(1), [0])

    def test_2(self):
        self.assertEqual(self.fib.fibonacci(2), [0, 1])

    def test_5(self):
        self.assertEqual(self.fib.fibonacci(5), [0, 1, 1, 2, 3])

    def test_negative(self):
        self.assertRaisesRegex(ValueError, "invalid input: out of range", self.fib.fibonacci, -1)

    def test_max(self):
        self.assertRaisesRegex(ValueError, "invalid input: out of range", self.fib.fibonacci, 10001)
    #
    def test_float(self):
        self.assertRaisesRegex(ValueError, "invalid input: not an integer", self.fib.fibonacci, 8.25)
    #
    def test_string(self):
        self.assertRaisesRegex(ValueError, "invalid input: not an integer", self.fib.fibonacci, "hi")


if __name__ == '__main__':
    unittest.main()