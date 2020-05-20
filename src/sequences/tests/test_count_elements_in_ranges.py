from sequences.count_elements_in_ranges import *


class TestCountElementsInRanges:
    def test_when_all_numbers_out_of_range_then_count_is_zero(self):
        assert count(
            nums=[0, 3, 12, 18],
            ranges=[[1, 2], [13, 17]]
        ) == 0

    def test_when_some_numbers_in_range_then_count_is_positive(self):
        assert count(
            nums=[0, 2, 14, 18],
            ranges=[[1, 3], [13, 17]]
        ) == 2
