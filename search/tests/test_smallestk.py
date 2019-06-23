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


class TestRank(unittest.TestCase):
    def test_given_k_is_less_than_1_then_raise_error(self):
        self.assertRaises(ValueError, rank, [1], 0)

    def test_given_k_is_greater_than_array_length_then_raise_error(self):
        self.assertRaises(ValueError, rank, [1], 2)

    def test_given_array_of_length_one(self):
        self.assertEqual(rank([1], k=1), 1)

    def test_given_array_of_length_two(self):
        self.assertEqual(rank([2, 1], k=1), 1)
        self.assertEqual(rank([2, 1], k=2), 2)

    def test_given_array_of_length_three(self):
        self.assertEqual(rank([3, 2, 1], k=1), 1)
        self.assertEqual(rank([3, 2, 1], k=2), 2)
        self.assertEqual(rank([3, 2, 1], k=3), 3)

    def test_given_array_with_duplicates(self):
        self.assertEqual(rank([3, 1, 1], k=1), 1)
        self.assertEqual(rank([3, 1, 1], k=2), 1)
        self.assertEqual(rank([3, 1, 1], k=3), 3)
        self.assertEqual(rank([3, 3, 3], k=1), 3)
        self.assertEqual(rank([3, 3, 3], k=2), 3)
        self.assertEqual(rank([3, 3, 3], k=3), 3)


class TestSmallest(unittest.TestCase):
    def test_given_k_is_less_than_1_then_raise_error(self):
        self.assertRaises(ValueError, smallest, [1], 0)

    def test_given_k_is_greater_than_array_length_then_raise_error(self):
        self.assertRaises(ValueError, smallest, [1], 2)

    def test_given_array_of_length_one(self):
        self.assertListEqual(smallest([1], k=1), [1])

    def test_given_array_of_length_two(self):
        self.assertListEqual(smallest([2, 1], k=1), [1])
        self.assertListEqual(smallest([2, 1], k=2), [1, 2])

    def test_given_array_of_length_three(self):
        self.assertListEqual(smallest([3, 2, 1], k=1), [1])
        self.assertListEqual(smallest([3, 2, 1], k=2), [1, 2])
        self.assertListEqual(smallest([3, 2, 1], k=3), [1, 2, 3])

    def test_given_array_with_duplicates(self):
        self.assertListEqual(smallest([3, 1, 1], k=1), [1])
        self.assertListEqual(smallest([3, 1, 1], k=2), [1, 1])
        self.assertListEqual(smallest([3, 1, 1], k=3), [1, 1, 3])
        self.assertListEqual(smallest([3, 3, 3], k=1), [3])
        self.assertListEqual(smallest([3, 3, 3], k=2), [3, 3])
        self.assertListEqual(smallest([3, 3, 3], k=3), [3, 3, 3])


if __name__ == '__main__':
    unittest.main()
