"""
Given two strings, find the length of longest subsequence present in both of them.
Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

SOLUTION
N is the maximum length of the two strings.

Recursive top-down approach.
- Time O(2^N)
- Space O(N^2): recursive call stack; store the intermediate result

Memoization approach.
- Time O(N^2)
- Space O(N^2)
"""
from typing import Set, Tuple, Dict


def _lcs_rec(s: str, t: str, i: int, j: int) -> Set[str]:
    res: Set[str] = set()
    if i == len(s) or j == len(t):
        return res
    if s[i] == t[j]:
        us = _lcs_rec(s, t, i + 1, j + 1)
        if len(us) == 0:
            res.add(s[i])
            return res
        for u in us:
            res.add(s[i] + u)
        return res
    us = _lcs_rec(s, t, i + 1, j)
    vs = _lcs_rec(s, t, i, j + 1)
    if len(us) == 0:
        return vs
    if len(vs) == 0:
        return us
    for u in us:
        for v in vs:
            if len(u) > len(v):
                return us
            if len(v) > len(u):
                return vs
            break
    return vs | us


def lcs_rec(s: str, t: str) -> Set[str]:
    if s is None or t is None:
        raise ValueError("strings s and t must not be None.")
    return _lcs_rec(s, t, 0, 0)


def _lcs_memo(
    s: str, t: str, i: int, j: int, memo: Dict[Tuple[int, int], Set[str]]
) -> Set[str]:
    res: Set[str] = set()
    if i == len(s) or j == len(t):
        return res
    if s[i] == t[j]:
        k = (i + 1, j + 1)
        if k not in memo:
            memo[k] = _lcs_rec(s, t, k[0], k[1])
        if len(memo[k]) == 0:
            res.add(s[i])
            return res
        for tmp in memo[k]:
            res.add(s[i] + tmp)
        return res
    k = (i + 1, j)
    if k not in memo:
        memo[k] = _lcs_rec(s, t, k[0], k[1])
    us = memo[k]
    k = (i, j + 1)
    if k not in memo:
        memo[k] = _lcs_rec(s, t, k[0], k[1])
    vs = memo[k]
    if len(us) == 0 and len(vs) == 0:
        return us
    if len(us) == 0:
        return vs
    if len(vs) == 0:
        return us
    for u in us:
        for v in vs:
            if len(u) > len(v):
                return us
            if len(v) > len(u):
                return vs
            break
    return vs | us


def lcs_memo(s: str, t: str) -> Set[str]:
    if s is None or t is None:
        raise ValueError("strings s and t must not be None.")
    memo: Dict[Tuple[int, int], Set[str]] = {}
    return _lcs_memo(s, t, 0, 0, memo)
