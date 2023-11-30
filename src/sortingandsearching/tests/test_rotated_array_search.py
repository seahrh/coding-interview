import pytest

from sortingandsearching.rotated_array_search import *


class TestRotatedArraySearch:
    def test_when_array_is_empty_then_not_found(self):
        assert find([], 1) == -1

    def test_when_array_is_length_one(self):
        assert find([1], 1) == 0
        assert find([1], -1) == -1

    def test_when_array_is_length_two(self):
        arr = [20, 10]
        assert find(arr, 10) == 1
        assert find(arr, 20) == 0
        assert find(arr, 11) == -1

    def test_when_array_is_length_three_and_min_is_middle(self):
        arr = [30, 10, 20]
        assert find(arr, 10) == 1
        assert find(arr, 20) == 2
        assert find(arr, 30) == 0
        assert find(arr, 11) == -1

    def test_when_array_is_length_three_and_min_is_last(self):
        arr = [20, 30, 10]
        assert find(arr, 10) == 2
        assert find(arr, 20) == 0
        assert find(arr, 30) == 1
        assert find(arr, 11) == -1

    def test_given_example(self):
        arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        assert find(arr, 15) == 0
        assert find(arr, 16) == 1
        assert find(arr, 19) == 2
        assert find(arr, 20) == 3
        assert find(arr, 25) == 4
        assert find(arr, 1) == 5
        assert find(arr, 3) == 6
        assert find(arr, 4) == 7
        assert find(arr, 5) == 8
        assert find(arr, 7) == 9
        assert find(arr, 10) == 10
        assert find(arr, 14) == 11
        assert find(arr, 11) == -1


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
