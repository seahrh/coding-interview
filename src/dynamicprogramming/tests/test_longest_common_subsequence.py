from dynamicprogramming.longest_common_subsequence import *


class TestLongestCommonSubsequence:
    def test_recursion(self):
        assert lcs_rec("", "") == set()
        assert lcs_rec("a", "") == set()
        assert lcs_rec("", "a") == set()
        assert lcs_rec("a", "a") == {"a"}
        assert lcs_rec("ef", "abcd") == set()
        assert lcs_rec("bd", "abcd") == {"bd"}
        assert lcs_rec("abdace", "babce") == {"bace", "abce"}
        assert lcs_rec("ABCDGH", "AEDFHR") == {"ADH"}
        assert lcs_rec("AGGTAB", "GXTXAYB") == {"GTAB"}

    def test_memoization(self):
        assert lcs_memo("", "") == set()
        assert lcs_memo("a", "") == set()
        assert lcs_memo("", "a") == set()
        assert lcs_memo("a", "a") == {"a"}
        assert lcs_memo("ef", "abcd") == set()
        assert lcs_memo("bd", "abcd") == {"bd"}
        assert lcs_memo("abdace", "babce") == {"bace", "abce"}
        assert lcs_memo("ABCDGH", "AEDFHR") == {"ADH"}
        assert lcs_memo("AGGTAB", "GXTXAYB") == {"GTAB"}
