"""
152. Maximum Product Subarray https://leetcode.com/problems/maximum-product-subarray/description/

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

SOLUTION

Time O(N)
Space O(N)
References
- https://leetcode.com/problems/maximum-product-subarray/solutions/183483/javacpython-it-can-be-more-simple/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = list(nums)
        suf = list(nums)
        # reset product to nums[i] if prefix[i-1] is zero
        for i in range(1, len(nums)):
            pre[i] *= pre[i - 1] or 1
        # reset product to nums[i] if suffix[i+1] is zero
        for i in range(len(nums) - 2, -1, -1):
            suf[i] *= suf[i + 1] or 1
        return max(pre + suf)
