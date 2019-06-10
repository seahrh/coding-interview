import unittest
from search.sorted_matrix_search import *


class TestSortedMatrixSearch(unittest.TestCase):
    def test_when_matrix_is_empty_then_raise_error(self):
        self.assertRaises(ValueError, find, [], 1)

    def test_when_matrix_is_1x1(self):
        self.assertEqual(find([[1]], 1), (0, 0))
        self.assertEqual(find([[1]], -1), -1)

    def test_when_matrix_is_2x2(self):
        self.assertEqual(find([[1, 2], [3, 4]], 1), (0, 0))
        self.assertEqual(find([[1, 2], [3, 4]], 2), (0, 1))
        self.assertEqual(find([[1, 2], [3, 4]], 3), (1, 0))
        self.assertEqual(find([[1, 2], [3, 4]], 4), (1, 1))
        self.assertEqual(find([[1, 2], [3, 4]], 30), -1)

    def test_when_matrix_is_3x3(self):
        matrix = [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ]
        self.assertEqual(find(matrix, 10), (0, 0))
        self.assertEqual(find(matrix, 20), (0, 1))
        self.assertEqual(find(matrix, 30), (0, 2))
        self.assertEqual(find(matrix, 40), (1, 0))
        self.assertEqual(find(matrix, 50), (1, 1))
        self.assertEqual(find(matrix, 60), (1, 2))
        self.assertEqual(find(matrix, 70), (2, 0))
        self.assertEqual(find(matrix, 80), (2, 1))
        self.assertEqual(find(matrix, 90), (2, 2))
        self.assertEqual(find(matrix, 51), -1)

    def test_when_matrix_is_4x4(self):
        matrix = [
            [10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120],
            [130, 140, 150, 160]
        ]
        self.assertEqual(find(matrix, 10), (0, 0))
        self.assertEqual(find(matrix, 20), (0, 1))
        self.assertEqual(find(matrix, 30), (0, 2))
        self.assertEqual(find(matrix, 40), (0, 3))
        self.assertEqual(find(matrix, 50), (1, 0))
        self.assertEqual(find(matrix, 60), (1, 1))
        self.assertEqual(find(matrix, 70), (1, 2))
        self.assertEqual(find(matrix, 80), (1, 3))
        self.assertEqual(find(matrix, 90), (2, 0))
        self.assertEqual(find(matrix, 100), (2, 1))
        self.assertEqual(find(matrix, 110), (2, 2))
        self.assertEqual(find(matrix, 120), (2, 3))
        self.assertEqual(find(matrix, 130), (3, 0))
        self.assertEqual(find(matrix, 140), (3, 1))
        self.assertEqual(find(matrix, 150), (3, 2))
        self.assertEqual(find(matrix, 160), (3, 3))
        self.assertEqual(find(matrix, 51), -1)


class TestSortedMatrixBinarySearch(unittest.TestCase):

    def test_when_matrix_is_empty_then_raise_error(self):
        self.assertRaises(ValueError, binary_search, [], 1)

    def test_when_matrix_is_1x1(self):
        self.assertEqual(binary_search([[1]], 1), Cell(0, 0))
        self.assertEqual(binary_search([[1]], -1), None)

    def test_when_matrix_is_2x2(self):
        matrix = [[10, 20], [30, 40]]
        self.assertEqual(binary_search(matrix, 10), Cell(0, 0))
        self.assertEqual(binary_search(matrix, 20), Cell(0, 1))
        self.assertEqual(binary_search(matrix, 30), Cell(1, 0))
        self.assertEqual(binary_search(matrix, 40), Cell(1, 1))
        self.assertEqual(binary_search(matrix, 11), None)

    def test_when_matrix_is_3x3(self):
        matrix = [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ]
        self.assertEqual(binary_search(matrix, 10), Cell(0, 0))
        self.assertEqual(binary_search(matrix, 20), Cell(0, 1))
        self.assertEqual(binary_search(matrix, 30), Cell(0, 2))
        self.assertEqual(binary_search(matrix, 40), Cell(1, 0))
        self.assertEqual(binary_search(matrix, 50), Cell(1, 1))
        self.assertEqual(binary_search(matrix, 60), Cell(1, 2))
        self.assertEqual(binary_search(matrix, 70), Cell(2, 0))
        self.assertEqual(binary_search(matrix, 80), Cell(2, 1))
        self.assertEqual(binary_search(matrix, 90), Cell(2, 2))
        self.assertEqual(binary_search(matrix, 51), None)

    def test_when_matrix_is_4x4(self):
        matrix = [
            [10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120],
            [130, 140, 150, 160]
        ]
        self.assertEqual(binary_search(matrix, 10), Cell(0, 0))
        self.assertEqual(binary_search(matrix, 20), Cell(0, 1))
        self.assertEqual(binary_search(matrix, 30), Cell(0, 2))
        self.assertEqual(binary_search(matrix, 40), Cell(0, 3))
        self.assertEqual(binary_search(matrix, 50), Cell(1, 0))
        self.assertEqual(binary_search(matrix, 60), Cell(1, 1))
        self.assertEqual(binary_search(matrix, 70), Cell(1, 2))
        self.assertEqual(binary_search(matrix, 80), Cell(1, 3))
        self.assertEqual(binary_search(matrix, 90), Cell(2, 0))
        self.assertEqual(binary_search(matrix, 100), Cell(2, 1))
        self.assertEqual(binary_search(matrix, 110), Cell(2, 2))
        self.assertEqual(binary_search(matrix, 120), Cell(2, 3))
        self.assertEqual(binary_search(matrix, 130), Cell(3, 0))
        self.assertEqual(binary_search(matrix, 140), Cell(3, 1))
        self.assertEqual(binary_search(matrix, 150), Cell(3, 2))
        self.assertEqual(binary_search(matrix, 160), Cell(3, 3))
        self.assertEqual(binary_search(matrix, 51), None)


if __name__ == '__main__':
    unittest.main()
