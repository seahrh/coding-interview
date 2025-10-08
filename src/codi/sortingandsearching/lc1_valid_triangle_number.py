"""
611. Valid Triangle Number https://leetcode.com/problems/valid-triangle-number/description/

Given an integer array nums, return the number of triplets chosen from the array that can make triangles
if we take them as side lengths of a triangle.
Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:
Input: nums = [4,2,3,4]
Output: 4
Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000

SOLUTION
Two pointers similar to 3Sum.

Time O(N^2)
Space O(1)
References
- https://leetcode.com/problems/valid-triangle-number/solutions/1339340/c-java-python-two-pointers-picture-explain-clean-concise-o-n-2/
"""

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # There are j-1 valid pairs because when k and j are fixed,
                    # nums[i]+nums[j]>nums[k] holds true when moving i to the right.
                    res += j - i
                    j -= 1
                    continue
                i += 1
        return res
