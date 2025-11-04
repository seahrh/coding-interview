"""
Remove Invalid Parentheses
==============================
Remove the minimum number of invalid parentheses in order to make the input string valid.
Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]

From
- https://leetcode.com/articles/remove-invalid-parentheses/
- https://kennyzhuang.gitbooks.io/algorithms-collection/content/remove_invalid_parentheses1.html

SOLUTION
DFS backtracking
Limit max removal rmL and rmR for backtracking boundary.
Otherwise it will exhaust all possible valid substrings, not shortest ones.
Scan from left to right, avoiding invalid strings (on the fly) by checking number of open parens.
If it's '(', either keep it or drop it.
If it's ')', either keep it or drop it.
Otherwise just append it.

Time O(2^N): since in the worst case we will have only left parentheses in the expression
and for every bracket we will have two options i.e. whether to remove it or consider it.
Space O(N): recursive call stack
"""

from typing import Set


def _remove(
    result: Set[str],
    s: str,
    index: int,
    left: int,
    right: int,
    num_open: int,
    partial: str,
) -> None:
    # Solution is complete and valid; add to result
    if index == len(s) and left == 0 and right == 0 and num_open == 0:
        result.add(partial)
        return
    # Not a possible solution; backtrack
    if index == len(s) or left < 0 or right < 0 or num_open < 0:
        return
    c = s[index]
    longer = partial + c
    if c == "(":
        _remove(result, s, index + 1, left - 1, right, num_open, partial)  # drop it
        _remove(result, s, index + 1, left, right, num_open + 1, longer)  # keep it
        return
    if c == ")":
        _remove(result, s, index + 1, left, right - 1, num_open, partial)  # drop it
        _remove(result, s, index + 1, left, right, num_open - 1, longer)  # keep it
        return
    _remove(result, s, index + 1, left, right, num_open, longer)


def remove(s: str) -> Set[str]:
    res: Set[str] = set()
    # number of left and right parentheses that can be dropped safely
    left = 0
    right = 0
    for c in s:
        if c == "(":
            left += 1
        if c == ")":
            if left != 0:
                left -= 1
            else:
                right += 1
    _remove(res, s, 0, left, right, 0, "")
    return res
