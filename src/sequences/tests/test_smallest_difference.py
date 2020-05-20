import pytest
from sequences.smallest_difference import *


class TestSmallestDifference:
    def test_when_array_is_empty_then_raise_error(self):
        with pytest.raises(ValueError):
            smallest_difference([], [1])

        with pytest.raises(ValueError):
            smallest_difference([1], [])

    def test_when_either_array_is_length_one(self):
        assert smallest_difference(
            a=[1],
            b=[1]
        ) == 0
        assert smallest_difference(
            a=[1],
            b=[3, 2]
        ) == 1
        assert smallest_difference(
            a=[3, 2],
            b=[1]
        ) == 1

    def test_when_arrays_are_length_two(self):
        assert smallest_difference(
            a=[10, 20],
            b=[5, 21]
        ) == 1

    def test_given_arrays_of_unequal_length_when_pair_is_last_element(self):
        assert smallest_difference(
            a=[10, 20, 30, 40],
            b=[7, 14, 25, 38, 39]
        ) == 1

    def test_given_example_1(self):
        assert smallest_difference(
            a=[1, 2, 3, 11, 15],
            b=[8, 9, 23, 127, 135]
        ) == 2

    def test_given_example_2(self):
        assert smallest_difference(
            a=[1, 2, 11, 15],
            b=[4, 12, 19, 23, 127, 135]
        ) == 1
