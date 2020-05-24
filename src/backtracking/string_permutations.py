"""
Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.
(8.7, p367)

SOLUTION
Backtracking without pruning: enumerate all possibilities.
Time O(N * N!)
- N recursive calls.
- Inserting the character takes factorial time because there are N! permutations (partials).
Space O(N): recursive call stack
"""
from typing import Set


def permutate_without_duplicates(remainder: str) -> Set[str]:
    res = set()
    if len(remainder) == 0:  # base case
        res.add("")
        return res
    head = remainder[0]
    partials = permutate_without_duplicates(remainder[1:])
    for p in partials:
        for i in range(len(p) + 1):  # also insert character at the end of the string!
            res.add(p[:i] + head + p[i:])
    return res
