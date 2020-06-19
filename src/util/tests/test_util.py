from util import *


class TestArgMin:
    def test_argmin(self):
        assert argmin([0]) == 0
        assert argmin([-1, -1, 0, 1, 0, 1]) == 0
        assert argmin([0, 1, -1, -1, 1, 0]) == 2
        assert argmin([0, 1, 1, 0, -1]) == 4
        assert argmin([0, 1, 1, 0, -1, -1]) == 4


class TestArgMax:
    def test_argmax(self):
        assert argmax([0]) == 0
        assert argmax([1, 1, -1, 0, -1, 0]) == 0
        assert argmax([-1, -1, 1, 1, 0, 0]) == 2
        assert argmax([0, -1, 0, -1, 1]) == 4
        assert argmax([0, -1, 0, -1, 1, 1]) == 4
