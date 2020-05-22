from dynamicprogramming.stairs import *


class TestStairs:
    def test_climb_recursive(self):
        assert climb_rec(n=1, steps={1}) == 1
        assert climb_rec(n=1, steps={2}) == 0
        assert climb_rec(n=4, steps={1, 2}) == 5
        assert climb_rec(n=4, steps={1, 2, 4}) == 6
        assert climb_rec(n=4, steps={1, 2, 5}) == 5
        assert climb_rec(n=5, steps={1, 2, 3}) == 13

        """n=6, steps={1, 2, 3}
        111 111
        33
        222
        12 111
        21 111
        11 211
        11 121
        11 112
        3 111
        111 3
        13 11
        11 31
        123
        132
        213
        231
        312
        321
        11 22
        22 11
        21 21
        21 12
        12 21
        12 12
        """
        assert climb_rec(n=6, steps={1, 2, 3}) == 24

    def test_climb_iterative(self):
        assert climb(n=1, steps={1}) == 1
        assert climb(n=1, steps={2}) == 0
        assert climb(n=4, steps={1, 2}) == 5
        assert climb(n=4, steps={1, 2, 4}) == 6
        assert climb(n=4, steps={1, 2, 5}) == 5
        assert climb(n=5, steps={1, 2, 3}) == 13
        assert climb(n=6, steps={1, 2, 3}) == 24
