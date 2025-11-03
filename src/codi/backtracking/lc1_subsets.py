"""
78. Subsets https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

SOLUTION
Each element can be either present or absent in a subset—essentially a binary decision (pick or not pick).
Use backtracking (recursive DFS), but no need to sort or use set();
the input array is unique, so subsets will also be unique if we build them in order.

Backtracking:
At every index, choose to include or exclude the element.
`path` is the current subset being built.
`result` collects all subsets.
For each decision:
Add the current path (this is one subset).
For each further number, add it and recurse, then remove it (backtrack).
No sorting needed (as input is unique and handled in order).
No sets needed (since input has no duplicates).
Time Complexity: O(2^N), since there are 2 ** n possible subsets.
Space Complexity: O(n) for the recursion stack (max depth).
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            # Add the current subset (path) to the result
            result.append(path[:])
            for i in range(start, len(nums)):
                # Include nums[i] in subset, recurse
                path.append(nums[i])
                backtrack(i + 1, path)
                # Backtrack: remove nums[i] and try next possibility
                path.pop()

        backtrack(0, [])
        return result
