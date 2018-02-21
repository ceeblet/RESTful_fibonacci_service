import unittest
from app import fibonacci


class test_fibonacci(unittest.TestCase):
    def test_min(self):
        self.assertEqual(fibonacci.fibonacci(1), [0])

    def test_2(self):
        self.assertEqual(fibonacci.fibonacci(2), [0, 1])

    def test_5(self):
        self.assertEqual(fibonacci.fibonacci(5), [0, 1, 1, 2, 3])

    def test_negative(self):
        self.assertRaisesRegex(ValueError, "invalid input: out of range", fibonacci.fibonacci, -1)

    def test_max(self):
        self.assertRaisesRegex(ValueError, "invalid input: out of range", fibonacci.fibonacci, 10001)
    #
    def test_float(self):
        self.assertRaisesRegex(ValueError, "invalid input: not an integer", fibonacci.fibonacci, 8.25)
    #
    def test_string(self):
        self.assertRaisesRegex(ValueError, "invalid input: not an integer", fibonacci.fibonacci, "hi")


if __name__ == '__main__':
    unittest.main()