"""
238. Product of Array Except Self https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

SOLUTION
You need two things for each index i:
The product of all numbers before i (“prefix”)
The product of all numbers after i (“suffix”)
Then, answer[i] = prefix[i] * suffix[i] for each index.
Explanation
First Loop: Store, for each i, the product of everything to the left of i.
Second Loop: In reverse, multiply by the product of everything to the right of i.
No division, two O(n) passes.
Use output array for extra space (which is allowed as per problem statement).
Time Complexity:
O(n) — two passes through the array
Space Complexity:
O(1) extra space excluding the result array (the result doesn’t count as extra).
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        # Calculate prefix products for each position
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        # Calculate suffix products for each position, multiplying as we go
        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
