"""
72. Edit Distance https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

SOLUTION
dp[i][j] = min number of moves to change a[:i+1] to b[:j+1]
Base case: both strings are empty, or 1 string has length 1
Recurrence:
- Add or delete: Moving up, down, left, right
- Replace char, dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
- If both chars are equal, then dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
Time O(MN)
Space O(MN)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[500] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                r = 1
                #  minus 1 bec dp is 1-indexed, so dp[0] means empty string!
                if word1[i - 1] == word2[j - 1]:
                    r = 0
                # min([add, delete, replace])
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + r)
        return dp[m][n]
