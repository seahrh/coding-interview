from sequences.duplicates import *


class TestDuplicates:
    def test_empty_strings(self):
        assert remove_duplicates("") == ""

    def test_strings_of_length_one(self):
        assert remove_duplicates("a") == "a"

    def test_when_no_duplicates_exist_then_return_original_string(self):
        assert remove_duplicates("abc") == "abc"

    def test_when_duplicates_exist_then_return_string_without_duplicates(self):
        assert remove_duplicates("aabc") == "abc"
        assert remove_duplicates("abca") == "abc"
        assert remove_duplicates("abac") == "abc"
