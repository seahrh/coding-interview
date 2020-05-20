from trees.heaps.shortest_supersequence import *


class TestShortestSupersequence:
    def test_given_not_all_includes_are_found_then_return_none(self):
        assert shortest_supersequence([1, 2, 3], includes={1, 4}) is None

    def test_given_empty_array_then_return_none(self):
        assert shortest_supersequence([], includes={1, 4}) is None

    def test_given_array_of_length_one(self):
        assert shortest_supersequence([1], includes={1}) == Range(0, 0)

    def test_given_array_of_length_two(self):
        assert shortest_supersequence([1, 2], includes={1}) == Range(0, 0)

    def test_given_includes_of_length_two(self):
        assert shortest_supersequence([1, 2], includes={1, 2}) == Range(0, 1)

    def test_given_example_1(self):
        assert shortest_supersequence(
            [7, 5, 9, 8, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], includes={1, 5, 9}
        ) == Range(7, 10)

    def test_given_result_covers_the_whole_array(self):
        assert shortest_supersequence(
            [1, 2, 3, 4, 5, 6, 7, 8], includes={1, 8}
        ) == Range(0, 7)
