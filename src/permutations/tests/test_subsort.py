import pytest
from sequences.subsort import *


class TestSubSort:
    def test_given_empty_array_then_raise_error(self):
        with pytest.raises(ValueError):
            subsort([])

    def test_given_array_of_length_one(self):
        assert subsort([1]) is None

    def test_given_array_of_length_two(self):
        assert subsort([1, 2]) is None
        assert subsort([2, 1]) == (0, 1)

    def test_given_array_of_length_three(self):
        assert subsort([1, 2, 3]) is None
        assert subsort([3, 2, 1]) == (0, 2)
        assert subsort([2, 1, 3]) == (0, 1)
        assert subsort([1, 3, 2]) == (1, 2)

    def test_given_array_of_length_four(self):
        assert subsort([1, 2, 3, 4]) is None
        assert subsort([4, 3, 2, 1]) == (0, 3)
        assert subsort([2, 3, 1, 4]) == (0, 2)
        assert subsort([2, 1, 3, 4]) == (0, 1)
        assert subsort([1, 3, 2, 4]) == (1, 2)
        assert subsort([1, 4, 2, 3]) == (1, 3)
        assert subsort([1, 2, 4, 3]) == (2, 3)

    def test_given_example_1(self):
        assert subsort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) == (3, 9)

    def test_given_example_2(self):
        assert subsort([30, 40, 39, 50]) == (1, 2)
