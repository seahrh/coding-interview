from recursion.longest_word import *


class TestLongestWord:
    def test_given_empty_array_then_return_none(self):
        assert longest_word([]) is None

    def test_given_example_1(self):
        assert longest_word(["ab", "a", "b", "abba"]) == "abba"

    def test_given_example_2(self):
        assert (
            longest_word(["spellingbeetest", "test", "spelling", "bee"])
            == "spellingbeetest"
        )
