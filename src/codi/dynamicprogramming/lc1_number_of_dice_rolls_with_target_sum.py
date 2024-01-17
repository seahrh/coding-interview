"""
1155. Number of Dice Rolls with Target Sum https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

You have n dice, and each die has k faces numbered from 1 to k.
Given three integers n, k, and target,
return the number of possible ways (out of the kn total ways) to roll the dice,
so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 10^9 + 7.
Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 10^9 + 7.
Constraints:
1 <= n, k <= 30
1 <= target <= 1000

SOLUTION
dp[i][j] = #ways to make sum i with the first j dices
# Base case: dp[1][1] = 1, dp[2][1] = 1, ... dp[k][1] = 1
# Recurrence: dp[i][j] = dp[i-1][j-1] + dp[i-2][j-1] + ... + dp[i-k][j-1]
Time O(TNK)
Space O(TN)
"""
from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod: int = int(1e9) + 7
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(target + 1)]
        for i in range(k):
            if i + 1 < target + 1:
                dp[i + 1][1] = 1
        for i in range(1, target + 1):
            for j in range(2, n + 1):
                for z in range(1, k + 1):
                    if i - z >= 0:
                        dp[i][j] += dp[i - z][j - 1]
                        dp[i][j] %= mod
        return dp[target][n]
