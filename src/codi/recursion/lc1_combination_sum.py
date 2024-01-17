"""
39. Combination Sum https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.
The test cases are generated such that
the number of unique combinations that sum up to target is less than 150 combinations for the given input.
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:
Input: candidates = [2], target = 1
Output: []
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

SOLUTION
we are not considering the whole array as possible options at every level, because we want unique combinations.
e.g. at the node [2, 2, 3], the possible options for the next level are only [3, 5].
Why?? because if we consider the whole array as possible options,
then we will get [2, 2, 3, 2] (with 2 as a possible option), which has already been checked as [2, 2, 2, 3].
So to make the solution unique, we only have to consider the subarray from current element to last element.
Base case: terminate if curr sum is greater than target, or partial solution is valid (equals target).
References
- https://leetcode.com/problems/combination-sum/solutions/1777569/full-explanation-with-state-space-tree-recursion-and-backtracking-well-explained-c/
"""
from typing import List


class Solution:
    def rec(
        self,
        candidates: List[int],
        target: int,
        i: int,
        ps: int,
        p: List[int],
        full: List[List[int]],
    ) -> None:
        if ps > target:
            return
        if ps == target:
            full.append(p)
            return
        for j in range(i, len(candidates)):
            p.append(candidates[j])
            self.rec(candidates, target, i=j, ps=sum(p), p=list(p), full=full)
            p.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        full: List[List[int]] = []
        self.rec(candidates, target, i=0, ps=0, p=[], full=full)
        return full
