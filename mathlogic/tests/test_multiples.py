import unittest
from mathlogic.multiples import *


class TestMultiples(unittest.TestCase):
    def test_given_k_is_less_than_one_then_raise_error(self):
        self.assertRaises(ValueError, kth_multiple, 0)

    def test_given_k_is_1(self):
        self.assertEqual(kth_multiple(1), 1)

    def test_given_k_is_5(self):
        self.assertEqual(kth_multiple(5), 9)

    def test_given_k_is_13(self):
        self.assertEqual(kth_multiple(13), 63)


if __name__ == '__main__':
    unittest.main()
