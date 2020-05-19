import unittest
from sequences.sequence_sum import *


class TestLargestSum(unittest.TestCase):
    def test_array_of_length_one(self):
        self.assertEqual(largest_sum([0]), 0)

    def test_given_example(self):
        self.assertEqual(largest_sum([2, -8, 3, -2, 4, -10]), 5)

    def test_array_with_all_negative_numbers(self):
        self.assertEqual(largest_sum([-2, -8, -3, -2, -4, -10]), -2)


class TestSequenceSumEquals(unittest.TestCase):
    def test_array_of_length_one(self):
        self.assertEqual(sequence_sum_equals(arr=[1], target=1), True)
        self.assertEqual(sequence_sum_equals(arr=[1], target=2), False)

    def test_found_sequence_at_tail(self):
        self.assertEqual(sequence_sum_equals(arr=[23, 5, 4, 7, 2, 11], target=20), True)
        self.assertEqual(sequence_sum_equals(arr=[23, 5, 4, 7, 2, 110], target=110), True)

    def test_found_sequence_in_the_middle(self):
        self.assertEqual(sequence_sum_equals(arr=[1, 3, 5, 23, 2], target=8), True)
        self.assertEqual(sequence_sum_equals(arr=[1, 3, 5, 230, 2], target=230), True)

    def test_found_sequence_at_head(self):
        self.assertEqual(sequence_sum_equals(arr=[1, 3, 5, 23, 2], target=1), True)
        self.assertEqual(sequence_sum_equals(arr=[1, 3, 5, 230, 2], target=4), True)

    def test_sequence_not_found(self):
        self.assertEqual(sequence_sum_equals(arr=[1, 3, 5, 23, 2], target=7), False)
        self.assertEqual(sequence_sum_equals(arr=[23, 5, 4, 7, 2, 11], target=19), False)


class TestSumSwap(unittest.TestCase):
    def test_given_empty_arrays(self):
        self.assertRaises(ValueError, sum_swap, [], [1])
        self.assertRaises(ValueError, sum_swap, [1], [])

    def test_given_either_array_of_length_one(self):
        self.assertEqual(sum_swap([1], [1]), (1, 1))
        self.assertEqual(sum_swap([1], [2]), None)
        self.assertEqual(sum_swap([2], [2, 4]), (2, 4))

    def test_given_either_array_of_length_two(self):
        self.assertEqual(sum_swap([1, 2], [2, 1]), (2, 2))
        self.assertEqual(sum_swap([4, 2], [3, 1]), (4, 3))
        self.assertEqual(sum_swap([1, 2], [3, 1]), None)
        self.assertEqual(sum_swap([1, 2], [3, 1, 5]), (2, 5))

    def test_given_example(self):
        self.assertEqual(sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]), (6, 4))


class TestSumSwapSorted(unittest.TestCase):
    def test_given_empty_arrays(self):
        self.assertRaises(ValueError, sum_swap_sorted, [], [1])
        self.assertRaises(ValueError, sum_swap_sorted, [1], [])

    def test_given_either_array_of_length_one(self):
        self.assertEqual(sum_swap_sorted([1], [1]), (1, 1))
        self.assertEqual(sum_swap_sorted([1], [2]), None)
        self.assertEqual(sum_swap_sorted([2], [2, 4]), (2, 4))

    def test_given_either_array_of_length_two(self):
        self.assertEqual(sum_swap_sorted([1, 2], [1, 2]), (1, 1))
        self.assertEqual(sum_swap_sorted([2, 4], [1, 3]), (2, 1))
        self.assertEqual(sum_swap_sorted([1, 2], [1, 3]), None)
        self.assertEqual(sum_swap_sorted([1, 2], [1, 3, 5]), (2, 5))

    def test_given_example(self):
        self.assertEqual(sum_swap_sorted([1, 1, 1, 2, 2, 4], [3, 3, 3, 6]), (1, 3))


if __name__ == '__main__':
    unittest.main()
