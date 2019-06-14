import unittest
from sequences.pair_sum import *


class TestPairSum(unittest.TestCase):
    def test_given_empty_array_then_return_empty_set(self):
        self.assertSetEqual(pair_sum(arr=[], summ=1), set())

    def test_when_array_length_is_one_then_return_empty_set(self):
        self.assertSetEqual(pair_sum(arr=[1], summ=1), set())

    def test_single_pair_found(self):
        self.assertSetEqual(pair_sum(arr=[1, 2], summ=3), {(1, 2)})
        self.assertSetEqual(pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=4), {(1, 3)})
        self.assertSetEqual(pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-5), {(-3, -2)})

    def test_many_pairs_found(self):
        self.assertSetEqual(pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=2), {(0, 2), (-1, 3)})
        self.assertSetEqual(pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-1), {(-3, 2), (-2, 1), (-1, 0)})


class TestHasPairSum(unittest.TestCase):
    def test_when_array_length_is_one_then_not_found(self):
        self.assertEqual(has_pair_sum(arr=[1], summ=1), False)

    def test_single_pair_found(self):
        self.assertEqual(has_pair_sum(arr=[1, 2], summ=3), True)
        self.assertEqual(has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=4), True)
        self.assertEqual(has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-5), True)

    def test_many_pairs_found(self):
        self.assertEqual(has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=2), True)
        self.assertEqual(has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-1), True)

    def test_when_duplicates_equal_sum_then_found(self):
        self.assertEqual(has_pair_sum(arr=[1, 2, 4, 4], summ=8), True)
        self.assertEqual(has_pair_sum(arr=[4, 1, 2, 4], summ=8), True)

    def test_when_duplicates_exist_and_pair_do_not_exist_then_not_found(self):
        self.assertEqual(has_pair_sum(arr=[1, 2, 4, 4], summ=7), False)
        self.assertEqual(has_pair_sum(arr=[4, 1, 2, 4], summ=7), False)


if __name__ == '__main__':
    unittest.main()
