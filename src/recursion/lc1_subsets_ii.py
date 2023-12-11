"""
90. Subsets II https://leetcode.com/problems/subsets-ii/description/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

SOLUTION
For each number, either pick or not pick. The path from root to leaf is 1 subset.
Time O(2^N)
Space O(N)
"""
from typing import List, Set, Tuple


class Solution:
    def rec(self, nums: List[int], i: int, p: List[int], full: Set[Tuple[int]]) -> None:
        if i == len(nums):  # base case
            p.sort()
            full.add(tuple(p))
            return
        self.rec(nums=nums, i=i + 1, p=list(p), full=full)
        p.append(nums[i])
        self.rec(nums=nums, i=i + 1, p=list(p), full=full)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        full = set()
        self.rec(nums=nums, i=0, p=[], full=full)
        return [list(s) for s in full]
