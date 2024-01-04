"""
55. Jump Game https://leetcode.com/problems/jump-game/description/

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

SOLUTION
dp[i] = True if you can reach the last index from the i-th index
Base case: False if ar[i]==0
Recurrence: dp[i]=dp[i+ar[i]]
Time O(NK) where K is the largest value in the array.
Space O(N)
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp: List[bool] = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]
