from searching.peak_valley import *


class TestPeak:
    def test_array_of_length_one(self):
        assert peak([1]) == 0

    def test_array_of_length_two(self):
        assert peak([1, 1]) == 0
        assert peak([1, 2]) == 1
        assert peak([2, 1]) == 0

    def test_array_of_length_three_or_greater(self):
        assert peak([1, 1, 1]) == 1
        assert peak([5, 10, 20, 15]) == 2
        assert peak([10, 20, 15, 2, 23, 90, 67]) == 1
        assert peak([8, 9, 10, 2, 5, 6]) == 2
        assert peak([8, 9, 10, 12, 15]) == 4
        assert peak([10, 8, 6, 5, 3, 2]) == 0


class TestValley:
    def test_array_of_length_one(self):
        assert valley([1]) == 0

    def test_array_of_length_two(self):
        assert valley([1, 1]) == 0
        assert valley([1, 2]) == 0
        assert valley([2, 1]) == 1

    def test_array_of_length_three_or_greater(self):
        assert valley([1, 1, 1]) == 1
        assert valley([5, 10, 20, 15]) == 0
        assert valley([10, 20, 15, 2, 23, 90, 67]) == 3
        assert valley([8, 9, 10, 2, 5, 6]) == 0
        assert valley([8, 9, 10, 12, 15]) == 0
        assert valley([10, 8, 6, 5, 3, 2]) == 5
