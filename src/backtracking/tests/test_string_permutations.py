from backtracking.string_permutations import *


class TestStringPermutations:
    def test_when_string_is_length_one(self):
        assert solve("a") == {"a"}

    def test_when_string_is_length_two(self):
        assert solve("ab") == {"ab", "ba"}

    def test_when_string_is_length_three(self):
        assert solve("abc") == {
            "abc",
            "bac",
            "bca",
            "acb",
            "cab",
            "cba",
        }

    def test_when_string_is_length_four(self):
        assert solve("abcd") == {
            "abcd",
            "bacd",
            "bcad",
            "bcda",
            "acbd",
            "cabd",
            "cbad",
            "cbda",
            "acdb",
            "cadb",
            "cdab",
            "cdba",
            "abdc",
            "badc",
            "bdac",
            "bdca",
            "adbc",
            "dabc",
            "dbac",
            "dbca",
            "adcb",
            "dacb",
            "dcab",
            "dcba",
        }
