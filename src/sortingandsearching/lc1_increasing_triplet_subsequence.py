"""
334. Increasing Triplet Subsequence https://leetcode.com/problems/increasing-triplet-subsequence/

Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

SOLUTION
Track the lower bound of the 1st and 2nd elements of subseq.
References
- https://leetcode.com/problems/increasing-triplet-subsequence/discuss/79004/Concise-Java-solution-with-comments
"""
import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = sys.maxsize
        b = sys.maxsize
        for i in range(len(nums)):
            # <= comparison bec. b > a
            # consider the case where array has all same values e.g. [1, 1, 1, 1]
            if nums[i] <= a:  # found a smaller or same value for 1st element
                a = nums[i]
                continue
            if nums[i] <= b:  # found a smaller or same value for 2nd element
                b = nums[i]
                continue
            if a != sys.maxsize and b != sys.maxsize:
                return True
        return False
