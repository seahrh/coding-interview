"""
448. Find All Numbers Disappeared in an Array https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:
Input: nums = [1,1]
Output: [2]
Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

SOLUTION
Cyclic sort: put number i in the correct index i-1 (since nums[i] is in the range [1, n])
Time O(N)
Space O(1)
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            j = nums[i]
            while nums[j - 1] != j:
                nums[i], nums[j - 1] = nums[j - 1], nums[i]
                j = nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
