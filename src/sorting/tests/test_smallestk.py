import pytest
from sorting.smallestk import *


class TestMedianOfThree:
    def test_given_empty_array_then_raise_error(self):
        with pytest.raises(IndexError):
            median_of_three([], lo=0, hi=1)

    def test_given_one_distinct_item_then_return_itself(self):
        assert median_of_three([10], lo=0, hi=0) == 10

    def test_given_two_distinct_items_then_return_either_item(self):
        assert median_of_three([10, 20], lo=0, hi=1) == 10
        assert median_of_three([20, 10], lo=0, hi=1) == 20
        assert median_of_three([20, 10, 10], lo=0, hi=2) == 10
        assert median_of_three([20, 10, 10, 20], lo=0, hi=3) == 20

    def test_given_three_distinct_items_then_return_middle_item(self):
        assert median_of_three([10, 20, 30], lo=0, hi=2) == 20
        assert median_of_three([20, 10, 30], lo=0, hi=2) == 20
        assert median_of_three([30, 10, 20], lo=0, hi=2) == 20


class TestRank:
    def test_given_k_is_less_than_1_then_raise_error(self):
        with pytest.raises(ValueError):
            rank([1], k=0)

    def test_given_k_is_greater_than_array_length_then_raise_error(self):
        with pytest.raises(ValueError):
            rank([1], k=2)

    def test_given_array_of_length_one(self):
        assert rank([1], k=1) == 1

    def test_given_array_of_length_two(self):
        assert rank([2, 1], k=1) == 1
        assert rank([2, 1], k=2) == 2

    def test_given_array_of_length_three(self):
        assert rank([3, 2, 1], k=1) == 1
        assert rank([3, 2, 1], k=2) == 2
        assert rank([3, 2, 1], k=3) == 3

    def test_given_array_with_duplicates(self):
        assert rank([3, 1, 1], k=1) == 1
        assert rank([3, 1, 1], k=2) == 1
        assert rank([3, 1, 1], k=3) == 3
        assert rank([3, 3, 3], k=1) == 3
        assert rank([3, 3, 3], k=2) == 3
        assert rank([3, 3, 3], k=3) == 3


class TestSmallest:
    def test_given_k_is_less_than_1_then_raise_error(self):
        with pytest.raises(ValueError):
            smallest([1], k=0)

    def test_given_k_is_greater_than_array_length_then_raise_error(self):
        with pytest.raises(ValueError):
            smallest([1], k=2)

    def test_given_array_of_length_one(self):
        assert smallest([1], k=1) == [1]

    def test_given_array_of_length_two(self):
        assert smallest([2, 1], k=1) == [1]
        assert smallest([2, 1], k=2) == [1, 2]

    def test_given_array_of_length_three(self):
        assert smallest([3, 2, 1], k=1) == [1]
        assert smallest([3, 2, 1], k=2) == [1, 2]
        assert smallest([3, 2, 1], k=3) == [1, 2, 3]

    def test_given_array_with_duplicates(self):
        assert smallest([3, 1, 1], k=1) == [1]
        assert smallest([3, 1, 1], k=2) == [1, 1]
        assert smallest([3, 1, 1], k=3) == [1, 1, 3]
        assert smallest([3, 3, 3], k=1) == [3]
        assert smallest([3, 3, 3], k=2) == [3, 3]
        assert smallest([3, 3, 3], k=3) == [3, 3, 3]
