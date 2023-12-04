import pytest

from sortingandsearching.lc1_search_in_rotated_sorted_array import *


class TestRotatedArraySearchMinimum:
    def test_when_array_is_empty_then_raise_error(self):
        with pytest.raises(ValueError):
            index_of_min([])

    def test_when_array_is_length_one(self):
        assert index_of_min([1]) == 0

    def test_when_array_is_length_two(self):
        assert index_of_min([2, 1]) == 1

    def test_when_array_is_length_three(self):
        assert index_of_min([3, 1, 2]) == 1
        assert index_of_min([2, 3, 1]) == 2

    def test_when_array_is_length_four(self):
        assert index_of_min([4, 1, 2, 3]) == 1
        assert index_of_min([3, 4, 1, 2]) == 2
        assert index_of_min([2, 3, 4, 1]) == 3
