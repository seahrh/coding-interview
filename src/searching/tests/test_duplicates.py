from searching.duplicates import *


class TestFindOneDuplicate:
    def test_shortest_array(self):
        assert find_one_duplicate([1, 1]) == 1

    def test_duplicate_in_the_middle(self):
        assert find_one_duplicate([1, 1, 2]) == 1
        assert find_one_duplicate([3, 1, 3, 4, 2]) == 3

    def test_duplicate_at_the_end(self):
        assert find_one_duplicate([1, 2, 2]) == 2
        assert find_one_duplicate([1, 2, 1]) == 1
        assert find_one_duplicate([1, 3, 4, 2, 2]) == 2
