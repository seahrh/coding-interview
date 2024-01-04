"""
91. Decode Ways https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped
then mapped back into letters using the reverse of the mapping above
(there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

SOLUTION
dp[i] = number of ways to decode the string starting at index i
Base case: dp[n]=1  there is one way to decode an empty string
Recurrence:
Decode single digit: dp[i] += dp[i + 1]
Decode double digits: dp[i] += dp[i + 2]
If current digit is zero, then dp[i]=0
References
- https://leetcode.com/problems/decode-ways/solutions/4454173/recursive-top-down-bottom-up-clean-and-commented-code-dynamic-programming/
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            j = int(s[i])
            if j == 0:
                dp[i] = 0
                continue
            dp[i] += dp[i + 1]  # decode single digit
            if i + 1 < n and int(s[i : i + 2]) <= 26:  # decode double digits
                dp[i] += dp[i + 2]
        return dp[0]
