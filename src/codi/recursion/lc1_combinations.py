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
For each number, either pick or not pick. The path from root to leaf represents 1 combination.
Base case: visited all numbers or partial solution has grown to full length.
Time O(2^N)
Space O(N)
References
- https://leetcode.com/problems/combinations/solutions/3845640/recursion-very-simple-pick-not-pick/
"""
from typing import List


class Solution:
    def rec(self, n: int, k: int, i: int, p: List[int], full: List[List[int]]) -> None:
        if i > n:
            if len(p) == k:
                full.append(p)
            return
        if len(p) == k:
            full.append(p)
            return
        self.rec(n, k, i + 1, list(p) + [i], full)
        self.rec(n, k, i + 1, list(p), full)

    def combine(self, n: int, k: int) -> List[List[int]]:
        full: List[List[int]] = []
        self.rec(n=n, k=k, i=1, p=[], full=full)
        return full
