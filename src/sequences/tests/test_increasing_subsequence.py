from sequences.increasing_subsequence import *


class TestIncreasingTriple:
    def test_when_array_length_is_less_than_3_then_return_none(self):
        assert increasing_triple([]) is None
        assert increasing_triple([1]) is None
        assert increasing_triple([1, 2]) is None

    def test_array_length_three_or_greater(self):
        assert increasing_triple([1, 2, 3]) == (0, 1, 2)
        assert increasing_triple([12, 11, 10, 5, 6, 2, 30]) == (3, 4, 6)
        assert increasing_triple([1, 2, 3, 4]) == (0, 1, 2)
        assert increasing_triple([4, 3, 1, 2]) is None
        assert increasing_triple([12, 1, 11, 10, 5, 4, 3]) is None
        assert increasing_triple([12, 1, 11, 10, 5, 4, 7]) == (1, 5, 6)
        assert increasing_triple([12, 11, 10, 5, 2, 4, 1, 3]) is None
        assert increasing_triple([12, 11, 10, 5, 2, 4, 1, 6]) == (4, 5, 7)
        assert increasing_triple([5, 13, 6, 10, 3, 7, 2]) == (0, 2, 3)
        assert increasing_triple([1, 5, 1, 5, 2, 2, 5]) == (0, 5, 6)
        assert increasing_triple([1, 5, 1, 5, 2, 1, 5]) == (0, 4, 6)
        assert increasing_triple([2, 3, 1, 4]) == (0, 1, 3)
        assert increasing_triple([3, 1, 2, 4]) == (1, 2, 3)
