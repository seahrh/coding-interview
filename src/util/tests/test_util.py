from util import *


class TestArgMin:
    def test_integer(self):
        assert argmin([0]) == 0
        assert argmin([-1, -1, 0, 1, 0, 1]) == 0
        assert argmin([0, 1, -1, -1, 1, 0]) == 2
        assert argmin([0, 1, 1, 0, -1]) == 4
        assert argmin([0, 1, 1, 0, -1, -1]) == 4

    def test_boolean(self):
        assert argmin([False]) == 0
        assert argmin([True]) == 0
        assert argmin([False, True]) == 0
        assert argmin([True, False]) == 1
        assert argmin([False, True, True, False]) == 0
        assert argmin([True, False, False, True]) == 1
        assert argmin([True, True, False]) == 2


class TestArgMax:
    def test_integer(self):
        assert argmax([0]) == 0
        assert argmax([1, 1, -1, 0, -1, 0]) == 0
        assert argmax([-1, -1, 1, 1, 0, 0]) == 2
        assert argmax([0, -1, 0, -1, 1]) == 4
        assert argmax([0, -1, 0, -1, 1, 1]) == 4

    def test_boolean(self):
        assert argmax([False]) == 0
        assert argmax([True]) == 0
        assert argmax([False, True]) == 1
        assert argmax([True, False]) == 0
        assert argmax([False, True, True, False]) == 1
        assert argmax([True, False, False, True]) == 0
        assert argmax([False, False, True]) == 2


class TestDotProduct:
    def test_matrix_with_1_row(self):
        assert dot([[1]], [[-1]]) == [[-1]]
        assert dot([[-1]], [[1]]) == [[-1]]
        assert dot([[1]], [[2]]) == [[2]]
        assert dot([[2]], [[1]]) == [[2]]

    def test_matrix_with_2_rows(self):
        p = [[1, 2], [3, 4]]
        q = [[1], [2]]
        assert dot(p, q) == [[5], [11]]
        p = [[1, 2], [3, 4]]
        q = [[3, 1], [2, 4]]
        assert dot(p, q) == [[7, 9], [17, 19]]
        assert dot(q, p) == [[6, 10], [14, 20]]
        p = [[1, 2], [3, 4]]
        q = [[2, 0], [1, 2]]
        assert dot(p, q) == [[4, 4], [10, 8]]
        assert dot(q, p) == [[2, 4], [7, 10]]

    def test_matrix_with_3_rows(self):
        p = [[1, 2, 3], [4, 5, 6]]
        q = [[7, 8], [9, 10], [11, 12]]
        assert dot(p, q) == [[58, 64], [139, 154]]
        p = [[3, 4, 2]]
        q = [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]]
        assert dot(p, q) == [[83, 63, 37, 75]]
        p = [[1, 2, 3]]
        q = [[4], [5], [6]]
        assert dot(p, q) == [[32]]
        assert dot(q, p) == [[4, 8, 12], [5, 10, 15], [6, 12, 18]]
        p = [[2, 0, -1], [3, 5, 2], [-4, 1, 4]]
        q = [[5, 1, -2], [-1, 0, 4], [2, -3, 3]]
        assert dot(p, q) == [
            [8, 5, -7],
            [14, -3, 20],
            [-13, -16, 24],
        ]
        assert dot(q, p) == [
            [21.0, 3.0, -11.0],
            [-18.0, 4.0, 17.0],
            [-17.0, -12.0, 4.0],
        ]
        p = [[3, -2, 5], [0, -1, 6], [-4, 2, -1]]
        q = [[2, -1, 0], [3, -5, 2], [1, 4, -2]]
        assert dot(p, q) == [[5.0, 27.0, -14.0], [3.0, 29.0, -14.0], [-3.0, -10.0, 6.0]]
        assert dot(q, p) == [[6.0, -3.0, 4.0], [1.0, 3.0, -17.0], [11.0, -10.0, 31.0]]
