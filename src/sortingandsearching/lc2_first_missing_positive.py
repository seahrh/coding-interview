"""
41. First Missing Positive https://leetcode.com/problems/first-missing-positive/description/

Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

SOLUTION
First missing positive is in the range [1,n], or n+1 if answer falls outside the range.
Time O(N)
Space O(1)
References
- https://leetcode.com/problems/first-missing-positive/solutions/2083286/python-o-n-time-o-1-space-step-by-step-explanation/
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Mark invalid answer as n+1
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        # If number j is present, mark the index j-1 as negative number
        # Get absolute value of the original number at index j-1 for evaluation
        for i in range(n):
            j = abs(nums[i])
            if j > n:
                continue
            nums[j - 1] = -abs(nums[j - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
