from sorting.count_distinct import *


class TestCountDistinct:
    def test_count_distinct(self):
        assert count_distinct([]) == 0
        assert count_distinct([1]) == 1
        assert count_distinct([1, 1]) == 1
        assert count_distinct([2, 1]) == 2
        assert count_distinct([2, 3, 2, 2, 3]) == 2
