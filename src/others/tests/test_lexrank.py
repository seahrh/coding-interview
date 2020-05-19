import pytest
from others.lexrank import *


class TestLexrank:
    def test_given_empty_string_then_raise_error(self):
        with pytest.raises(ValueError):
            rank('')

    def test_given_string_of_length_one_then_return_rank_1(self):
        assert rank('z') == 1

    def test_given_string_of_length_two(self):
        assert rank('ab') == 1
        assert rank('ba') == 2

    def test_given_string_of_length_three(self):
        assert rank('abc') == 1
        assert rank('acb') == 2
        assert rank('bac') == 3
        assert rank('bca') == 4
        assert rank('cab') == 5
        assert rank('cba') == 6

    def test_given_string_of_length_six(self):
        assert rank('string') == 598
