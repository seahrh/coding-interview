import unittest
from search.sorted_matrix_search import *


class TestSortedMatrixSearch(unittest.TestCase):
    def test_when_matrix_is_empty_then_raise_error(self):
        self.assertRaises(ValueError, find, [], 1)

    def test_when_matrix_is_1x1(self):
        self.assertEqual(find([[1]], 1), (0, 0))
        self.assertEqual(find([[1]], -1), -1)

    def test_when_matrix_is_2x2(self):
        self.assertEqual(find([[1, 2], [3, 4]], 3), (1, 0))
        self.assertEqual(find([[1, 2], [3, 4]], 30), -1)

    def test_when_matrix_is_3x3(self):
        self.assertEqual(find([
            [1, 2, 30],
            [2, 3, 40],
            [30, 40, 50]
        ], 3), (1, 1))
        self.assertEqual(find([
            [1, 2, 30],
            [2, 3, 40],
            [30, 40, 50]
        ], 31), -1)

    def test_when_matrix_is_4x4(self):
        self.assertEqual(find([
            [1, 2, 30, 40],
            [2, 3, 40, 50],
            [30, 40, 50, 60],
            [40, 50, 60, 70]
        ], 3), (1, 1))
        self.assertEqual(find([
            [1, 2, 30, 40],
            [2, 3, 40, 50],
            [30, 40, 50, 60],
            [40, 50, 60, 70]
        ], 31), -1)


if __name__ == '__main__':
    unittest.main()
