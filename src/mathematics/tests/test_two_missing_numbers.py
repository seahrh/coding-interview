from mathematics.two_missing_numbers import *


class TestTwoMissingNumbers:
    def test_missing_numbers_at_the_ends(self):
        assert solve(10, [9, 8, 7, 6, 4, 5, 3, 2]) == (1, 10)
        assert solve(10, [8, 7, 6, 4, 5, 3, 2, 1]) == (9, 10)
        assert solve(10, [8, 7, 6, 4, 5, 3, 9, 10]) == (1, 2)

    def test_missing_numbers_in_the_middle(self):
        assert solve(4, [4, 1]) == (2, 3)
        assert solve(10, [10, 9, 8, 7, 6, 5, 3, 1]) == (2, 4)
        assert solve(10, [10, 7, 6, 4, 5, 3, 2, 1]) == (8, 9)
