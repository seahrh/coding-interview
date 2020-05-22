from dynamicprogramming.stairs import *


class TestStairs:
    def test_climb(self):
        assert climb(n=1, steps={1}) == 1
        assert climb(n=1, steps={2}) == 0
        assert climb(n=4, steps={1, 2}) == 5
        assert climb(n=4, steps={1, 2, 4}) == 6
        assert climb(n=4, steps={1, 2, 5}) == 5
