import unittest
from recursion.fibonacci import *


class TestFibonacci(unittest.TestCase):
    def test_1st_fib_number(self):
        self.assertEqual(fib(1), 0)

    def test_2nd_fib_number(self):
        self.assertEqual(fib(2), 1)

    def test_7th_fib_number(self):
        self.assertEqual(fib(7), 8)
