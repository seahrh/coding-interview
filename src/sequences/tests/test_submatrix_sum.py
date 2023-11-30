import pytest

from sequences.submatrix_sum import *


class TestSubmatrixSum:
    def test_given_empty_matrix_then_raise_error(self):
        with pytest.raises(ValueError):
            max_submatrix([[]])

    def test_given_1x1_matrix(self):
        assert max_submatrix([[1]]) == Submatrix(
            top_left=Cell(row=0, col=0), bottom_right=Cell(row=0, col=0), sum=1
        )

    def test_given_2x2_matrix(self):
        assert max_submatrix([[1, -2], [10, 2]]) == Submatrix(
            top_left=Cell(row=1, col=0), bottom_right=Cell(row=1, col=1), sum=12
        )

    def test_given_2x3_matrix(self):
        assert max_submatrix([[1, -2, 10], [10, -2, 2]]) == Submatrix(
            top_left=Cell(row=0, col=0), bottom_right=Cell(row=1, col=2), sum=19
        )

    def test_given_3x5_matrix(self):
        assert max_submatrix(
            [[9, -8, 1, 3, -2], [-3, 7, 6, -2, 4], [6, -4, -4, 8, -7]]
        ) == Submatrix(
            top_left=Cell(row=0, col=0), bottom_right=Cell(row=2, col=3), sum=19
        )
