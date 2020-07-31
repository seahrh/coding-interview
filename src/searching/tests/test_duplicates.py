from searching.duplicates import *


class TestFindOneDuplicate:
    def test_shortest_array(self):
        assert find_one([1, 1]) == 1

    def test_duplicate_in_the_middle(self):
        assert find_one([1, 1, 2]) == 1
        assert find_one([3, 1, 3, 4, 2]) == 3

    def test_duplicate_at_the_end(self):
        assert find_one([1, 2, 2]) == 2
        assert find_one([1, 2, 1]) == 1
        assert find_one([1, 3, 4, 2, 2]) == 2


class TestFindTwoDuplicates:
    def test_shortest_array(self):
        assert find_two([1, 1, 2, 2]) == (1, 2)
        assert find_two([2, 2, 1, 1]) == (2, 1)
        assert find_two([1, 2, 1, 2]) == (1, 2)
        assert find_two([2, 1, 2, 1]) == (2, 1)

    def test_duplicate_in_the_middle(self):
        assert find_two([3, 1, 3, 4, 1, 2]) == (3, 1)
        assert find_two([3, 1, 1, 3, 4, 2]) == (1, 3)

    def test_duplicate_at_the_end(self):
        assert find_two([1, 3, 4, 4, 2, 2]) == (4, 2)
        assert find_two([2, 1, 4, 3, 4, 2]) == (4, 2)
