from codi.sequences.shortest_winter import *


class TestShortestWinter:
    def test_length(self):
        assert shortest_winter([1, 2]) == 1
        assert shortest_winter([2, 1]) == 1
        assert shortest_winter([5, -2, 3, 8, 6]) == 3
        assert shortest_winter([-5, -5, -5, -42, 6, 12]) == 4
        # last element has the smallest value; so longest winter
        assert shortest_winter([-5, -5, -42, 6, 12, -50]) == 5
