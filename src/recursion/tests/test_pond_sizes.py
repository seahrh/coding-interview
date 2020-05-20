from recursion.pond_sizes import *


class TestPondSizes:
    def test_given_empty_matrix_then_return_empty_list(self):
        assert pond_sizes([]) == []
        assert pond_sizes([[]]) == []

    def test_given_1x1_matrix(self):
        assert pond_sizes([[1]]) == []
        assert pond_sizes([[0]]) == [1]

    def test_given_2x2_matrix(self):
        assert pond_sizes([[1, 1], [1, 1]]) == []
        assert pond_sizes([[0, 1], [1, 1]]) == [1]
        assert pond_sizes([[1, 0], [1, 1]]) == [1]
        assert pond_sizes([[1, 1], [0, 1]]) == [1]
        assert pond_sizes([[1, 1], [1, 0]]) == [1]
        assert pond_sizes([[0, 0], [1, 1]]) == [2]
        assert pond_sizes([[0, 1], [0, 1]]) == [2]
        assert pond_sizes([[0, 1], [1, 0]]) == [2]
        assert pond_sizes([[0, 0], [0, 1]]) == [3]
        assert pond_sizes([[1, 0], [0, 0]]) == [3]
        assert pond_sizes([[0, 0], [0, 0]]) == [4]

    def test_given_2x5_matrix(self):
        assert pond_sizes([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == []
        assert pond_sizes([[0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [1]
        assert pond_sizes([[0, 1, 0, 1, 1], [1, 1, 0, 1, 0]]) == [1, 2, 1]
        assert pond_sizes([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == [10]

    def test_given_example(self):
        assert pond_sizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]) == [
            2,
            4,
            1,
        ]
