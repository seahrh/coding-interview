from searching.count_values_in_range import *


class TestCountValuesInRange:
    def test_arrays_of_length_2_or_less(self):
        assert count([1], lower=1, upper=2) == 1
        assert count([1], lower=2, upper=2) == 0
        assert count([2, 1], lower=1, upper=2) == 2
        assert count([3, 1], lower=1, upper=2) == 1
        assert count([3, 4], lower=1, upper=2) == 0

    def test_arrays_of_length_3_or_greater(self):
        assert count([1, 3, 3, 9, 10, 4], lower=1, upper=4) == 4
        assert count([1, 3, 3, 9, 10, 4], lower=9, upper=12) == 2
        assert count([1, 3, 3, 9, 10, 4], lower=4, upper=10) == 3
