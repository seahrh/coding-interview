"""
77. Combinations https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.
Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
Constraints:
1 <= n <= 20
1 <= k <= n

SOLUTION
For each number, either pick or not pick. The path from root to leaf contains 1 or more combinations.
Time O(2^N)
Space O(N)
"""
from typing import List, Set, Tuple


class Solution:
    def rec(
        self, n: int, k: int, i: int, p: List[int], full: Set[Tuple[int, ...]]
    ) -> None:
        if i > n:  # base case
            return
        self.rec(n, k, i + 1, list(p), full)
        p.append(i)
        if len(p) == k:
            p.sort()
            full.add(tuple(p))
            p = []
        self.rec(n, k, i + 1, list(p), full)

    def combine(self, n: int, k: int) -> List[List[int]]:
        full: Set[Tuple[int, ...]] = set()
        self.rec(n=n, k=k, i=1, p=[], full=full)
        return [list(c) for c in full]
