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
We are generating all permutations — every possible ordering of elements in nums.
At each recursive call, we choose one number that hasn’t been used yet,
then recursively build the rest of the permutation.
Time O(N * N!)
Each permutation takes O(N) to build, and there are N! permutations
Space O(N)
The recursion stack and path list hold at most N elements
"""

from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path: List[int], used: Set[int]):
            # Base case: full-length permutation
            if len(path) == len(nums):
                res.append(path[:])  # make a copy
                return
            # Try each unused number
            for num in nums:
                if num in used:
                    continue
                path.append(num)
                used.add(num)
                backtrack(path, used)
                path.pop()  # backtrack
                used.remove(num)

        backtrack([], set())
        return res
