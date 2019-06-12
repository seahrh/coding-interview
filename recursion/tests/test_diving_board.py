import unittest
from recursion.diving_board import *


class TestDivingBoardRecursive(unittest.TestCase):
    def test_when_k_is_less_than_1_then_raise_error(self):
        self.assertRaises(ValueError, all_lengths_rec, 0, 1, 2)

    def test_when_k_equals_1(self):
        self.assertSetEqual(all_lengths_rec(k=1, shorter=1, longer=2), {1, 2})

    def test_when_k_equals_2(self):
        self.assertSetEqual(all_lengths_rec(k=2, shorter=1, longer=2), {2, 3, 4})

    def test_when_k_equals_3(self):
        self.assertSetEqual(all_lengths_rec(k=3, shorter=1, longer=2), {3, 4, 5, 6})

    def test_when_k_equals_4(self):
        self.assertSetEqual(all_lengths_rec(k=4, shorter=1, longer=2), {4, 5, 6, 7, 8})


if __name__ == '__main__':
    unittest.main()
