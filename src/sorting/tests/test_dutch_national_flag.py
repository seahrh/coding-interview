import pytest
from sorting.dutch_national_flag import *


class TestDutchNationalFlag:
    def test_array_of_length_one(self):
        arr = [0]
        dutch_sort(arr)
        assert arr == [0]

    def test_array_with_less_than_three_colours(self):
        arr = [0, 0]
        dutch_sort(arr)
        assert arr == [0, 0]
        arr = [1, 0]
        dutch_sort(arr)
        assert arr == [0, 1]

    def test_array_with_three_colours(self):
        arr = [0, 1, 2]
        dutch_sort(arr)
        assert arr == [0, 1, 2]
        arr = [2, 1, 0]
        dutch_sort(arr)
        assert arr == [0, 1, 2]
        arr = [0, 1, 1, 1, 0, 0, 1, 2, 2, 0, 2, 1, 1, 2]
        dutch_sort(arr)
        assert arr == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]


class TestDutchNationalFlagFourColors:
    def test_array_of_length_one(self):
        arr = [0]
        dutch_sort_four_colors(arr)
        assert arr == [0]

    @pytest.mark.skip
    def test_array_with_less_than_four_colours(self):
        arr = [0, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 0]
        arr = [1, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 1]
        arr = [2, 1, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 1, 2]
