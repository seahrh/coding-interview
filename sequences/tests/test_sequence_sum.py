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


if __name__ == '__main__':
    unittest.main()
