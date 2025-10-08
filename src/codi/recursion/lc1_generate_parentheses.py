"""
22. Generate Parentheses https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
Constraints:
1 <= n <= 8

SOLUTION
Base case: partial solution has reached full length
Time O(2^N): 2N positions to fill and max 2 choices for each position
Space O(N): depth of recursive stack
References
- https://leetcode.com/problems/generate-parentheses/solutions/3290261/i-bet-you-will-understand-intutive-solution-beginner-friendly-c/
"""

from typing import List


class Solution:
    def rec(self, n: int, nop: int, ncl: int, p: str, full: List[str]) -> None:
        if len(p) == n * 2:
            full.append(p)
            return
        if nop == ncl:
            self.rec(n=n, nop=nop + 1, ncl=ncl, p=str(p) + "(", full=full)
            return
        if nop == n:
            self.rec(n=n, nop=nop, ncl=ncl + 1, p=str(p) + ")", full=full)
            return
        self.rec(n=n, nop=nop + 1, ncl=ncl, p=str(p) + "(", full=full)
        self.rec(n=n, nop=nop, ncl=ncl + 1, p=str(p) + ")", full=full)

    def generateParenthesis(self, n: int) -> List[str]:
        full: List[str] = []
        self.rec(n=n, nop=0, ncl=0, p="", full=full)
        return full
