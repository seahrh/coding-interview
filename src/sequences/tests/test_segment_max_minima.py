from sequences.segment_max_minima import *


class TestSegmentMaxMinima:
    def test_array_of_length_one(self):
        assert segment(x=1, arr=[1]) == 1

    def test_segment_of_length_two(self):
        assert segment(x=2, arr=[3, 4, 2]) == 3
        assert segment(x=2, arr=[4, 3]) == 3
        assert segment(x=2, arr=[6, 4, 1, 1, 1, 3, 8]) == 4

    def test_segment_of_length_three(self):
        assert segment(x=3, arr=[3, 4, 2, 1]) == 2
        assert segment(x=3, arr=[4, 3, 2]) == 2
        assert segment(x=3, arr=[6, 4, 1, 1, 1, 3, 8]) == 1
