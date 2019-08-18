import unittest
from searching.rotated_array_search import *


class TestRotatedArraySearch(unittest.TestCase):
    def test_when_array_is_empty_then_not_found(self):
        self.assertEqual(find([], 1), -1)

    def test_when_array_is_length_one(self):
        self.assertEqual(find([1], 1), 0)
        self.assertEqual(find([1], -1), -1)

    def test_when_array_is_length_two(self):
        arr = [20, 10]
        self.assertEqual(find(arr, 10), 1)
        self.assertEqual(find(arr, 20), 0)
        self.assertEqual(find(arr, 11), -1)

    def test_when_array_is_length_three_and_min_is_middle(self):
        arr = [30, 10, 20]
        self.assertEqual(find(arr, 10), 1)
        self.assertEqual(find(arr, 20), 2)
        self.assertEqual(find(arr, 30), 0)
        self.assertEqual(find(arr, 11), -1)

    def test_when_array_is_length_three_and_min_is_last(self):
        arr = [20, 30, 10]
        self.assertEqual(find(arr, 10), 2)
        self.assertEqual(find(arr, 20), 0)
        self.assertEqual(find(arr, 30), 1)
        self.assertEqual(find(arr, 11), -1)

    def test_given_example(self):
        arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEqual(find(arr, 15), 0)
        self.assertEqual(find(arr, 16), 1)
        self.assertEqual(find(arr, 19), 2)
        self.assertEqual(find(arr, 20), 3)
        self.assertEqual(find(arr, 25), 4)
        self.assertEqual(find(arr, 1), 5)
        self.assertEqual(find(arr, 3), 6)
        self.assertEqual(find(arr, 4), 7)
        self.assertEqual(find(arr, 5), 8)
        self.assertEqual(find(arr, 7), 9)
        self.assertEqual(find(arr, 10), 10)
        self.assertEqual(find(arr, 14), 11)
        self.assertEqual(find(arr, 11), -1)


class TestRotatedArraySearchMinimum(unittest.TestCase):
    def test_when_array_is_empty_then_raise_error(self):
        self.assertRaises(ValueError, index_of_min, [])

    def test_when_array_is_length_one(self):
        self.assertEqual(index_of_min([1]), 0)

    def test_when_array_is_length_two(self):
        self.assertEqual(index_of_min([2, 1]), 1)

    def test_when_array_is_length_three(self):
        self.assertEqual(index_of_min([3, 1, 2]), 1)
        self.assertEqual(index_of_min([2, 3, 1]), 2)

    def test_when_array_is_length_four(self):
        self.assertEqual(index_of_min([4, 1, 2, 3]), 1)
        self.assertEqual(index_of_min([3, 4, 1, 2]), 2)
        self.assertEqual(index_of_min([2, 3, 4, 1]), 3)


if __name__ == '__main__':
    unittest.main()
