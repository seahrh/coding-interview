import unittest
from sequences.pair_sum import *


class TestPairSum(unittest.TestCase):
    def test_when_array_length_is_one_then_return_empty_set(self):
        self.assertSetEqual(pairs(arr=[1], summ=1), set())

    def test_single_pair_found(self):
        self.assertSetEqual(pairs(arr=[1, 2], summ=3), {(0, 1)})
        self.assertSetEqual(pairs(arr=[2, -1, 3, -2, 1, -3, 0], summ=4), {(2, 4)})
        self.assertSetEqual(pairs(arr=[2, -1, 3, -2, 1, -3, 0], summ=-5), {(3, 5)})

    def test_many_pairs_found(self):
        self.assertSetEqual(pairs(arr=[2, -1, 3, -2, 1, -3, 0], summ=2), {(0, 6), (1, 2)})
        self.assertSetEqual(pairs(arr=[2, -1, 3, -2, 1, -3, 0], summ=-1), {(0, 5), (3, 4), (1, 6)})


if __name__ == '__main__':
    unittest.main()
