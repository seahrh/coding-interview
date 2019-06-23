import unittest
from search.smallestk import *


class TestMedianOfThree(unittest.TestCase):
    def test_given_empty_array_then_raise_error(self):
        self.assertRaises(IndexError, median_of_three, [], 0, 1)

    def test_given_one_distinct_item_then_return_itself(self):
        self.assertEqual(median_of_three([10], lo=0, hi=0), 10)

    def test_given_two_distinct_items_then_return_either_item(self):
        self.assertEqual(median_of_three([10, 20], lo=0, hi=1), 10)
        self.assertEqual(median_of_three([20, 10], lo=0, hi=1), 20)
        self.assertEqual(median_of_three([20, 10, 10], lo=0, hi=2), 10)
        self.assertEqual(median_of_three([20, 10, 10, 20], lo=0, hi=3), 20)

    def test_given_three_distinct_items_then_return_middle_item(self):
        self.assertEqual(median_of_three([10, 20, 30], lo=0, hi=2), 20)
        self.assertEqual(median_of_three([20, 10, 30], lo=0, hi=2), 20)
        self.assertEqual(median_of_three([30, 10, 20], lo=0, hi=2), 20)


if __name__ == '__main__':
    unittest.main()
