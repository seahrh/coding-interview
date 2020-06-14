from sorting.dutch_national_flag import *


class TestDutchNationalFlag:
    def test_array_of_length_one(self):
        arr = [0]
        dutch_sort(arr)
        assert arr == [0]

    def test_two_colours(self):
        arr = [0, 0]
        dutch_sort(arr)
        assert arr == [0, 0]
        arr = [1, 0]
        dutch_sort(arr)
        assert arr == [0, 1]
        arr = [2, 0]
        dutch_sort(arr)
        assert arr == [0, 2]
        arr = [2, 1]
        dutch_sort(arr)
        assert arr == [1, 2]

    def test_three_colours(self):
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

    def test_two_colours(self):
        arr = [0, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 0]
        arr = [1, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 1]
        arr = [2, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 2]
        arr = [2, 1]
        dutch_sort_four_colors(arr)
        assert arr == [1, 2]

    def test_three_colours(self):
        arr = [2, 1, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 1, 2]
        arr = [2, 1, 3]
        dutch_sort_four_colors(arr)
        assert arr == [1, 2, 3]
        arr = [2, 0, 3]
        dutch_sort_four_colors(arr)
        assert arr == [0, 2, 3]
        arr = [1, 0, 3]
        dutch_sort_four_colors(arr)
        assert arr == [0, 1, 3]

    def test_four_colours(self):
        arr = [0, 1, 2, 3]
        dutch_sort_four_colors(arr)
        assert arr == [0, 1, 2, 3]
        arr = [2, 1, 3, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 1, 2, 3]
        arr = [0, 1, 3, 1, 0, 0, 3, 2, 2, 0, 2, 1, 1, 2, 3, 3, 2, 0]
        dutch_sort_four_colors(arr)
        assert arr == [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
