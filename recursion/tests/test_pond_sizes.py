import unittest
from recursion.pond_sizes import *


class TestPondSizes(unittest.TestCase):
    def test_given_empty_matrix_then_return_empty_list(self):
        self.assertListEqual(pond_sizes([]), [])
        self.assertListEqual(pond_sizes([[]]), [])

    def test_given_1x1_matrix(self):
        self.assertListEqual(pond_sizes([[1]]), [])
        self.assertListEqual(pond_sizes([[0]]), [1])

    def test_given_2x2_matrix(self):
        self.assertListEqual(pond_sizes([[1, 1], [1, 1]]), [])
        self.assertListEqual(pond_sizes([[0, 1], [1, 1]]), [1])
        self.assertListEqual(pond_sizes([[1, 0], [1, 1]]), [1])
        self.assertListEqual(pond_sizes([[1, 1], [0, 1]]), [1])
        self.assertListEqual(pond_sizes([[1, 1], [1, 0]]), [1])
        self.assertListEqual(pond_sizes([[0, 0], [1, 1]]), [2])
        self.assertListEqual(pond_sizes([[0, 1], [0, 1]]), [2])
        self.assertListEqual(pond_sizes([[0, 1], [1, 0]]), [2])
        self.assertListEqual(pond_sizes([[0, 0], [0, 1]]), [3])
        self.assertListEqual(pond_sizes([[1, 0], [0, 0]]), [3])
        self.assertListEqual(pond_sizes([[0, 0], [0, 0]]), [4])

    def test_given_2x5_matrix(self):
        self.assertListEqual(pond_sizes([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]), [])
        self.assertListEqual(pond_sizes([[0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]), [1])
        self.assertListEqual(pond_sizes([[0, 1, 0, 1, 1], [1, 1, 0, 1, 0]]), [1, 2, 1])
        self.assertListEqual(pond_sizes([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]), [10])

    def test_given_example(self):
        self.assertListEqual(pond_sizes(
            [[0, 2, 1, 0],
             [0, 1, 0, 1],
             [1, 1, 0, 1],
             [0, 1, 0, 1]]), [2, 4, 1])


if __name__ == '__main__':
    unittest.main()
