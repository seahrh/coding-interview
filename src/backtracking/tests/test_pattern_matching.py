import pytest

from backtracking.pattern_matching import *


class TestPatternMatching:
    def test_given_empty_pattern_then_raise_error(self):
        with pytest.raises(ValueError):
            matches(pattern="", value="value")

    def test_given_empty_value_then_return_false(self):
        assert not matches(pattern="a", value="")

    def test_given_single_pattern_a_then_return_true(self):
        assert matches(pattern="a", value="value")

    def test_given_single_pattern_b_then_return_true(self):
        assert matches(pattern="b", value="value")

    def test_given_example(self):
        value = "catcatgocatgo"
        assert matches(pattern="aabab", value=value)
        assert matches(pattern="aab", value=value)
        assert matches(pattern="abb", value=value)
        assert matches(pattern="ab", value=value)
        assert matches(pattern="a", value=value)
        assert matches(pattern="b", value=value)
        assert not matches(pattern="aba", value=value)
        assert not matches(pattern="aaba", value=value)
