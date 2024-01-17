"""
20. Valid Parentheses https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be **closed in the correct order.**
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        st: List[str] = []
        for c in s:
            if c in "([{":
                st.append(c)
            elif c == ")":
                if len(st) == 0 or st[-1] != "(":
                    return False
                st.pop()
            elif c == "}":
                if len(st) == 0 or st[-1] != "{":
                    return False
                st.pop()
            elif c == "]":
                if len(st) == 0 or st[-1] != "[":
                    return False
                st.pop()
        return len(st) == 0
