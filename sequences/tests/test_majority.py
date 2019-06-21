import unittest
from sequences.majority import *


class TestMajority(unittest.TestCase):
    def test_given_empty_array_then_return_none(self):
        self.assertEqual(majority_element([]), None)

    def test_given_array_of_length_one(self):
        self.assertEqual(majority_element([1]), 1)

    def test_given_array_of_length_two(self):
        self.assertEqual(majority_element([1, 1]), 1)
        self.assertEqual(majority_element([1, -1]), None)

    def test_given_example_1(self):
        self.assertEqual(majority_element([1, 2, 5, 9, 5, 9, 5, 5, 5]), 5)

    def test_given_most_frequent_item_is_not_majority_then_return_none(self):
        self.assertEqual(majority_element([3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]), None)

    def test_given_most_frequent_item_is_majority_then_return_item(self):
        self.assertEqual(majority_element([3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7, 7, 7]), 7)


if __name__ == '__main__':
    unittest.main()
