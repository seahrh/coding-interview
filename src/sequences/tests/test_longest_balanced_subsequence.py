import pytest

from sequences.longest_balanced_subsequence import *


class TestLongestBalancedSubsequence:
    @staticmethod
    def _is_left(char):
        return char == "a"

    @staticmethod
    def _is_right(char):
        return char == "1"

    def test_given_unknown_char_then_raise_error(self):
        with pytest.raises(ValueError):
            longest_balanced_subsequence(
                arr=["@", "1"],
                is_left=TestLongestBalancedSubsequence._is_left,
                is_right=TestLongestBalancedSubsequence._is_right,
            )

    def test_given_array_of_length_one_then_return_none(self):
        assert (
            longest_balanced_subsequence(
                arr=["a"],
                is_left=TestLongestBalancedSubsequence._is_left,
                is_right=TestLongestBalancedSubsequence._is_right,
            )
            is None
        )
        assert (
            longest_balanced_subsequence(
                arr=["1"],
                is_left=TestLongestBalancedSubsequence._is_left,
                is_right=TestLongestBalancedSubsequence._is_right,
            )
            is None
        )

    def test_given_array_of_length_two(self):
        assert longest_balanced_subsequence(
            arr=["a", "1"],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right,
        ) == ["a", "1"]
        assert longest_balanced_subsequence(
            arr=["1", "a"],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right,
        ) == ["1", "a"]
        assert (
            longest_balanced_subsequence(
                arr=["a", "a"],
                is_left=TestLongestBalancedSubsequence._is_left,
                is_right=TestLongestBalancedSubsequence._is_right,
            )
            is None
        )
        assert (
            longest_balanced_subsequence(
                arr=["1", "1"],
                is_left=TestLongestBalancedSubsequence._is_left,
                is_right=TestLongestBalancedSubsequence._is_right,
            )
            is None
        )

    def test_given_example(self):
        assert longest_balanced_subsequence(
            arr=[
                "a",
                "a",
                "a",
                "a",
                "1",
                "1",
                "a",
                "1",
                "1",
                "a",
                "a",
                "1",
                "a",
                "a",
                "1",
                "a",
                "a",
                "a",
                "a",
                "a",
            ],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right,
        ) == ["a", "1", "1", "a", "1", "1", "a", "a", "1", "a", "a", "1"]
