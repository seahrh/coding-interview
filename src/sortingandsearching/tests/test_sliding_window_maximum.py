from sortingandsearching.sliding_window_maximum import *


class TestSlidingWindowMaximum:
    def test_case_1(self):
        assert solve(k=2, arr=[2, 1, 1, 2]) == [2, 1, 2]

    def test_case_2(self):
        assert solve(k=3, arr=[1, 3, -1, -3, 5, 3, 6, 7]) == [3, 3, 5, 5, 6, 7]

    def test_case_3(self):
        assert solve(k=3, arr=[1, 2, 3, 1, 4, 5, 2, 3, 6]) == [3, 3, 4, 5, 5, 5, 6]
