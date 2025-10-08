"""
53. Maximum Subarray https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
SOLUTION
If sum drops below zero, that subsequence will not contribute to the maximal subarray
since max is reduced by adding the negative sum.
If the array contains all negative numbers, sum is reset for each element,
effectively picking the smallest negative number.
Time O(N)
Space O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = int(-1e5)
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            res = max(res, sm)
            sm = max(sm, 0)
        return res
