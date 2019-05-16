import unittest
from sequences.sequence_sum import *


class TestLargestSum(unittest.TestCase):
    def test_array_of_length_one(self):
        self.assertEqual(largest_sum([0]), 0)

    def test_given_example(self):
        self.assertEqual(largest_sum([2, -8, 3, -2, 4, -10]), 5)

    def test_array_with_all_negative_numbers(self):
        self.assertEqual(largest_sum([-2, -8, -3, -2, -4, -10]), -2)


if __name__ == '__main__':
    unittest.main()
