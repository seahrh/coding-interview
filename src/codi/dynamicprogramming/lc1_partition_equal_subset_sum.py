"""
416. Partition Equal Subset Sum https://leetcode.com/problems/partition-equal-subset-sum/description/

Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or false otherwise.
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100

SOLUTION
Run 0-1 knapsack to get the number of ways to reach n(n+1)/4 using subsets of the numbers 1..n-1
Why n-1? Because by considering numbers up to n-1, we always put n in the second set,
and therefore only count each pair of sets once (otherwise we count every pair of sets twice).
dp[i][j] = number of ways to form subset sum j from the first i numbers
Base case: empty set to make sum 0, dp[i][0] = 1
The rest of the first row, dp[0][j] = 0
Recurrence: dp[i][j] = dp[i - 1][j] + dp[i - 1][j - i]
Either take the ith number or not.
Time O(N^2)
Space O(N^2): memo table
See https://codeforces.com/blog/entry/70018
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 == 1:
            return False
        sm = sm // 2
        n = len(nums)
        dp = [[False] * (sm + 1) for _ in range(n + 1)]
        for i in range(n + 1):  # base case: always possible to make zero sum
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, sm + 1):
                # already make sum j without i-th number
                dp[i][j] = dp[i - 1][j]
                # check if i-th number can make sum j
                if not dp[i][j] and j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]]
        return dp[n][sm]
