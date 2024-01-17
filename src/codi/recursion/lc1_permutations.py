"""
46. Permutations https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

SOLUTION
Consider all numbers for each position in permutation.
Base case: permutation grown to full length.
Time O(N!)
Space O(N)
References
- https://leetcode.com/problems/permutations/solutions/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning/
"""
from typing import List


class Solution:
    def rec(self, nums: List[int], p: List[int], full: List[List[int]]):
        if len(p) == len(nums):
            full.append(p)
            return
        for i in range(len(nums)):
            if nums[i] in p:  # skip duplicate element in subsequent positions
                continue
            p.append(nums[i])
            self.rec(nums=nums, p=list(p), full=full)
            p.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        full: List[List[int]] = []
        self.rec(nums=nums, p=[], full=full)
        return full
