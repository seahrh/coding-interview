from permutations.three_sum import *


class TestThreeSum:
    def test_three_sum(self):
        assert three_sum([]) == set()
        assert three_sum([1]) == set()
        assert three_sum([1, 1, 1]) == set()
        assert three_sum([-1, 0, 1, 2, -1, -4]) == {Triple(-1, 0, 1), Triple(-1, -1, 2)}
