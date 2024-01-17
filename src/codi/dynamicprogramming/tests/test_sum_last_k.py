from codi.dynamicprogramming.sum_last_k import *


class TestSumLastK:
    def test_example_1(self):
        assert solve(A=[1, 2, 3, 4, 5], k=2) == [1, 3, 5, 7, 9]

    def test_example_2(self):
        assert solve(A=[1, 2, 3, 4, 1, 2, 3, 4], k=3) == [1, 3, 6, 9, 8, 7, 6, 9]

    def test_only_one_element(self):
        assert solve(A=[1], k=1) == [1]
