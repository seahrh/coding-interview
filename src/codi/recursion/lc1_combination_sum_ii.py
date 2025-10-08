"""
40. Combination Sum II https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

SOLUTION
References
- https://leetcode.com/problems/combination-sum-ii/solutions/4370842/easy-understandable-c-solution/
- https://leetcode.com/problems/combination-sum-ii/solutions/1277764/combination-sum-i-ii-and-iii-subsets-i-and-ii-permutations-i-and-ii-one-stop-c-solutions/
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
        prev = -1
        for j in range(i, len(candidates)):
            # prevent duplicate combinations
            # do not pick same element for certain k-th position of a combination
            if candidates[j] != prev:
                p.append(candidates[j])
                # j+1 bec cannot reuse same element
                self.rec(candidates, target, i=j + 1, ps=sum(p), p=list(p), full=full)
                p.pop()
                prev = candidates[j]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        full: List[List[int]] = []
        self.rec(candidates, target, i=0, ps=0, p=[], full=full)
        return full
