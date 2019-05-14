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


class TestBinarySearchArrayWithEmptyStrings(unittest.TestCase):
    def test_search_array_of_length_one(self):
        self.assertEqual(search_array_with_empty_strings(arr=['b'], key='b'), 0)
        self.assertEqual(search_array_with_empty_strings(arr=['b'], key='a'), -1)
        self.assertEqual(search_array_with_empty_strings(arr=['b'], key='c'), -1)

    def test_search_array_of_length_two(self):
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c'], key='b'), 0)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c'], key='c'), 1)
        self.assertEqual(search_array_with_empty_strings(arr=['b', ''], key='b'), 0)
        self.assertEqual(search_array_with_empty_strings(arr=['', 'c'], key='c'), 1)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c'], key='a'), -1)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c'], key='d'), -1)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'd'], key='c'), -1)

    def test_search_array_of_length_three(self):
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c', 'd'], key='b'), 0)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c', 'd'], key='c'), 1)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c', 'd'], key='d'), 2)
        self.assertEqual(search_array_with_empty_strings(arr=['b', '', 'd'], key='b'), 0)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c', ''], key='c'), 1)
        self.assertEqual(search_array_with_empty_strings(arr=['', 'c', 'd'], key='d'), 2)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c', 'd'], key='a'), -1)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'c', 'd'], key='e'), -1)
        self.assertEqual(search_array_with_empty_strings(arr=['b', 'd', 'e'], key='c'), -1)

    def test_when_array_has_only_empty_strings_then_not_found(self):
        self.assertEqual(search_array_with_empty_strings(arr=[''], key='a'), -1)
        self.assertEqual(search_array_with_empty_strings(arr=['', ''], key='a'), -1)


class TestBinarySearchNearest(unittest.TestCase):
    def test_search_array_of_length_one(self):
        self.assertEqual(nearest(arr=[1], key=1), 0)
        self.assertEqual(nearest(arr=[1], key=0), 0)
        self.assertEqual(nearest(arr=[1], key=2), 0)

    def test_search_array_of_length_two(self):
        self.assertEqual(nearest(arr=[1, 2], key=1), 0)
        self.assertEqual(nearest(arr=[1, 2], key=2), 1)
        self.assertEqual(nearest(arr=[1, 2], key=0), 0)
        self.assertEqual(nearest(arr=[1, 2], key=3), 1)
        self.assertEqual(nearest(arr=[1, 4], key=2), 0)
        self.assertEqual(nearest(arr=[1, 4], key=3), 1)

    def test_search_array_of_length_three(self):
        arr = [1, 2, 3]
        self.assertEqual(nearest(arr=arr, key=1), 0)
        self.assertEqual(nearest(arr=arr, key=2), 1)
        self.assertEqual(nearest(arr=arr, key=3), 2)
        self.assertEqual(nearest(arr=arr, key=0), 0)
        self.assertEqual(nearest(arr=arr, key=4), 2)
        self.assertEqual(nearest(arr=[1, 2, 40], key=39), 2)
        self.assertEqual(nearest(arr=[1, 2, 40], key=3), 1)


if __name__ == '__main__':
    unittest.main()
