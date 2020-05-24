from backtracking.string_permutations import *


class TestStringPermutationsWithoutDuplicates:
    def test_when_string_is_empty_then_return_array_with_an_empty_string(self):
        assert permutate_without_duplicates("") == {""}

    def test_when_string_is_length_one(self):
        assert permutate_without_duplicates("a") == {"a"}

    def test_when_string_is_length_two(self):
        assert permutate_without_duplicates("ab") == {"ab", "ba"}

    def test_when_string_is_length_three(self):
        assert permutate_without_duplicates("abc") == {
            "abc",
            "bac",
            "bca",
            "acb",
            "cab",
            "cba",
        }

    def test_when_string_is_length_four(self):
        assert permutate_without_duplicates("abcd") == {
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
