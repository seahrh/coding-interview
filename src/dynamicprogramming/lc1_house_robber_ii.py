"""
213. House Robber II https://leetcode.com/problems/house-robber-ii/description/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:
Input: nums = [1,2,3]
Output: 3
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000

SOLUTION
Cannot take the first house if the last house is taken (and vice versa). Run dp twice.
References
- https://leetcode.com/problems/house-robber-ii/solutions/3219244/c-dp-beats-100-space-optimization/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def r1(nums: List[int]) -> int:
            n = len(nums)
            dp = [0] * (n + 1)
            dp[1] = nums[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            return dp[n]

        return max(r1(nums[:-1]), r1(nums[1:]))
