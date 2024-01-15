"""
131. Palindrome Partitioning https://leetcode.com/problems/palindrome-partitioning/description/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.

SOLUTION
Backtracking: partial solution represents the DFS path from root (empty solution) to leaf.
e.g. p1=["a","a","b"], p2=["aa","b"]]
Time O(2^N*N)
Space O(N)
References
- https://www.youtube.com/watch?v=3jvWodd7ht0
- https://leetcode.com/problems/palindrome-partitioning/solutions/3084800/c-backtracking-easy-to-understand/
"""
from copy import deepcopy
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: List[List[str]] = []
        partial: List[str] = []

        def is_palindrome(s, lo, hi) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        def dfs(i: int) -> None:
            nonlocal res, partial
            if i >= len(s):
                res.append(deepcopy(partial))  # partial solution is non-empty
                return
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):  # bounding function
                    partial.append(s[i : j + 1])
                    dfs(j + 1)
                    partial.pop()  # rewind the DFS path before backtracking

        dfs(0)
        return res
