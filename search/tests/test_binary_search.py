import unittest
from search.BinarySearch import *


class TestBinarySearch(unittest.TestCase):
    def test_search_array_of_length_one(self):
        self.assertEqual(search(arr=[1], key=1), 0)
        self.assertEqual(search(arr=[1], key=0), -1)
        self.assertEqual(search(arr=[1], key=2), -1)

    def test_search_array_of_length_two(self):
        self.assertEqual(search(arr=[1, 2], key=1), 0)
        self.assertEqual(search(arr=[1, 2], key=2), 1)
        self.assertEqual(search(arr=[1, 2], key=0), -1)
        self.assertEqual(search(arr=[1, 2], key=3), -1)
        self.assertEqual(search(arr=[1, 3], key=2), -1)

    def test_search_array_of_length_three(self):
        arr = [1, 2, 3]
        self.assertEqual(search(arr=arr, key=1), 0)
        self.assertEqual(search(arr=arr, key=2), 1)
        self.assertEqual(search(arr=arr, key=3), 2)
        self.assertEqual(search(arr=arr, key=0), -1)
        self.assertEqual(search(arr=arr, key=4), -1)
        self.assertEqual(search(arr=[1, 2, 4], key=3), -1)


if __name__ == '__main__':
    unittest.main()
