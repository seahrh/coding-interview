from sequences.divisibility_of_strings import *


class TestDivisibilityOfStrings:
    def test_case_1(self):
        assert solve("bcdbcdbcdbcd", "bcdbcd") == 3

    def test_case_2(self):
        assert solve("bcdbcdbcd", "bcdbcd") == -1

    def test_equal_strings(self):
        assert solve("abcd", "abcd") == 4
