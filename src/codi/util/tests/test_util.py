from codi.util import *


class TestArgMin:
    def test_integer(self):
        assert argmin([0]) == 0
        assert argmin([-1, -1, 0, 1, 0, 1]) == 0
        assert argmin([0, 1, -1, -1, 1, 0]) == 2
        assert argmin([0, 1, 1, 0, -1]) == 4
        assert argmin([0, 1, 1, 0, -1, -1]) == 4

    def test_boolean(self):
        assert argmin([False]) == 0
        assert argmin([True]) == 0
        assert argmin([False, True]) == 0
        assert argmin([True, False]) == 1
        assert argmin([False, True, True, False]) == 0
        assert argmin([True, False, False, True]) == 1
        assert argmin([True, True, False]) == 2


class TestArgMax:
    def test_integer(self):
        assert argmax([0]) == 0
        assert argmax([1, 1, -1, 0, -1, 0]) == 0
        assert argmax([-1, -1, 1, 1, 0, 0]) == 2
        assert argmax([0, -1, 0, -1, 1]) == 4
        assert argmax([0, -1, 0, -1, 1, 1]) == 4

    def test_boolean(self):
        assert argmax([False]) == 0
        assert argmax([True]) == 0
        assert argmax([False, True]) == 1
        assert argmax([True, False]) == 0
        assert argmax([False, True, True, False]) == 1
        assert argmax([True, False, False, True]) == 0
        assert argmax([False, False, True]) == 2
