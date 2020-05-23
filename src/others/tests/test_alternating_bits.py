from others.alternating_bits import *


class TestAlternatingBits:
    def test_min_flips(self):
        assert min_flips([0]) == 0
        assert min_flips([1]) == 0
        assert min_flips([0, 1, 0]) == 0
        assert min_flips([0, 0, 1]) == 1
        assert min_flips([0, 1, 1, 0]) == 2
        assert min_flips([1, 0, 1, 0, 1, 1]) == 1
        assert min_flips([1, 1, 0, 1, 1]) == 2
        assert min_flips([0, 0, 0, 1, 0, 1, 0, 1, 1, 1]) == 2
