from codi.others.sum_strings_without_addition import *


class TestSumStringsWithoutAddition:
    def test_case_1(self):
        assert solve("0", "1") == "1"
        assert solve("123", "1") == "124"
        assert solve("123", "7") == "130"
        assert solve("123", "30") == "153"
        assert solve("123", "877") == "1000"
        assert solve("999", "1") == "1000"
        assert solve("199", "1") == "200"
