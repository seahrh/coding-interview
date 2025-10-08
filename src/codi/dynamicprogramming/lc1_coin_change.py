"""
322. Coin Change https://leetcode.com/problems/coin-change/description/

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = [2], amount = 3
Output: -1
Example 3:
Input: coins = [1], amount = 0
Output: 0
Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 10^4

SOLUTION
dp[i] = min #coins to make sum i
We look at the last coin added to get sum x, say it has value v.
We need dp[x-v] coins to get value x-v, and 1 coin for value v.
Therefore we need dp[x-v]+1 coins if we are to use a coin with value v.
Time O(N lg N + XN)
Space O(X): memo array
References
- https://codeforces.com/blog/entry/70018
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        coins.sort()
        impossible = n + 1
        dp = [impossible] * (n + 1)
        dp[0] = 0
        for i in range(coins[0], n + 1):
            # consider all coins <= current target
            # also checks (i - cs[j] >= 0) to prevent IndexOutOfBounds!
            for c in coins:
                if c > i:
                    break
                dp[i] = min(dp[i], dp[i - c] + 1)
        res = dp[n]
        if res == impossible:
            res = -1
        return res
