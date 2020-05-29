import pytest
from sequences.sequence_sum import *


class TestLargestSum:
    def test_array_of_length_one(self):
        assert largest_sum([0]) == 0

    def test_given_example(self):
        assert largest_sum([2, -8, 3, -2, 4, -10]) == 5

    def test_array_with_all_negative_numbers(self):
        assert largest_sum([-2, -8, -3, -2, -4, -10]) == -2


class TestSequenceSumEquals:
    def test_array_of_length_one(self):
        assert sequence_sum_equals(arr=[1], target=1)
        assert not sequence_sum_equals(arr=[1], target=2)

    def test_found_sequence_at_tail(self):
        assert sequence_sum_equals(arr=[23, 5, 4, 7, 2, 11], target=20)
        assert sequence_sum_equals(arr=[23, 5, 4, 7, 2, 110], target=110)

    def test_found_sequence_in_the_middle(self):
        assert sequence_sum_equals(arr=[1, 3, 5, 23, 2], target=8)
        assert sequence_sum_equals(arr=[1, 3, 5, 230, 2], target=230)

    def test_found_sequence_at_head(self):
        assert sequence_sum_equals(arr=[1, 3, 5, 23, 2], target=1)
        assert sequence_sum_equals(arr=[1, 3, 5, 230, 2], target=4)

    def test_sequence_not_found(self):
        assert not sequence_sum_equals(arr=[1, 3, 5, 23, 2], target=7)
        assert not sequence_sum_equals(arr=[23, 5, 4, 7, 2, 11], target=19)


class TestSumSwap:
    def test_given_empty_arrays(self):
        with pytest.raises(ValueError):
            sum_swap([], [1])

        with pytest.raises(ValueError):
            sum_swap([1], [])

    def test_given_either_array_of_length_one(self):
        assert sum_swap([1], [1]) == (1, 1)
        assert sum_swap([1], [2]) is None
        assert sum_swap([2], [2, 4]) == (2, 4)

    def test_given_either_array_of_length_two(self):
        assert sum_swap([1, 2], [2, 1]) == (2, 2)
        assert sum_swap([4, 2], [3, 1]) == (4, 3)
        assert sum_swap([1, 2], [3, 1]) is None
        assert sum_swap([1, 2], [3, 1, 5]) == (2, 5)

    def test_given_example(self):
        assert sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]) == (6, 4)


class TestSumSwapSorted:
    def test_given_empty_arrays(self):
        with pytest.raises(ValueError):
            sum_swap_sorted([], [1])

        with pytest.raises(ValueError):
            sum_swap_sorted([1], [])

    def test_given_either_array_of_length_one(self):
        assert sum_swap_sorted([1], [1]) == (1, 1)
        assert sum_swap_sorted([1], [2]) is None
        assert sum_swap_sorted([2], [2, 4]) == (2, 4)

    def test_given_either_array_of_length_two(self):
        assert sum_swap_sorted([1, 2], [1, 2]) == (1, 1)
        assert sum_swap_sorted([2, 4], [1, 3]) == (2, 1)
        assert sum_swap_sorted([1, 2], [1, 3]) is None
        assert sum_swap_sorted([1, 2], [1, 3, 5]) == (2, 5)

    def test_given_example(self):
        assert sum_swap_sorted([1, 1, 1, 2, 2, 4], [3, 3, 3, 6]) == (1, 3)
