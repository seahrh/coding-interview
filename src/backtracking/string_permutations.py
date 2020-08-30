"""
Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.
(8.7, p367)
Constraints: 1 <= N <= 8
See https://cses.fi/problemset/task/1622

SOLUTION
Backtracking without pruning: enumerate all possibilities.
Time O(N * N!)
- N recursive calls.
- Inserting the character takes factorial time because there are N! permutations (partials).
Space O(N): recursive call stack
"""
from typing import Set


def _solve(remainder: str, result: Set[str]) -> None:
    if len(remainder) == 1:  # base case
        result.add(remainder)
        return
    head = remainder[0]
    # pass a new empty set to store the partial solutions
    partials: Set[str] = set()
    _solve(remainder[1:], partials)
    for p in partials:
        for i in range(len(p) + 1):
            result.add(p[:i] + head + p[i:])


def solve(s: str) -> Set[str]:
    res: Set[str] = set()
    _solve(s, res)
    return res
