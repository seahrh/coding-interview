from permutations.shortest_winter import *


class TestShortestWinter:
    def test_length(self):
        assert length([1, 2]) == 1
        assert length([2, 1]) == 1
        assert length([5, -2, 3, 8, 6]) == 3
        assert length([-5, -5, -5, -42, 6, 12]) == 4
        # last element has the smallest value; so longest winter
        assert length([-5, -5, -42, 6, 12, -50]) == 5
