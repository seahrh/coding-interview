"""
47. Permutations II https://leetcode.com/problems/permutations-ii/description/

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10

SOLUTION
Consider all numbers for each position in permutation.
Base case: permutation grown to full length.
Time O(N!)
Space O(N)
References
- https://leetcode.com/problems/permutations/solutions/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning/
"""
from typing import List, Set, Tuple


class Solution:
    def rec(
        self,
        nums: List[int],
        p: List[int],
        full: Set[Tuple[int, ...]],
        used: List[bool],
    ):
        if len(p) == len(nums):
            full.add(tuple(p))
            return
        for i in range(len(nums)):
            if used[i]:  # skip element that has already been added to partial solution
                continue
            p.append(nums[i])
            used[i] = True
            self.rec(nums=nums, p=list(p), full=full, used=used)
            p.pop()
            used[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used: List[bool] = [False] * len(nums)
        full: Set[Tuple[int, ...]] = set()
        self.rec(nums=nums, p=[], full=full, used=used)
        return [list(p) for p in full]
