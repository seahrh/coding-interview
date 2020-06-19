"""
Subset Sum
=============
Given a SET of non-negative integers, and a value sum C, find a subset with sum equal to C.
Variant of 0/1 Knapsack problem where all items have the same value per unit weight.

If multiple solutions exist, return any one of them.

SOLUTION: Dynamic programming (tabulation)
Time O(NC)
Space O(NC)

Backtracking (Time O(2^N)) is slower than DP but finds all solutions.
"""
from typing import List, Set

from util import argmax


def subset_sum(capacity: int, weights: Set[int]) -> Set[int]:
    n = len(weights)
    w_list = list(weights)
    # table[i][j] is True if subset with sum j can be obtained with items [1..i]
    table: List[List[bool]] = [[False] * (capacity + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            item = i - 1
            remainder = j - w_list[item]
            add_item = remainder >= 0 and table[i - 1][remainder]
            table[i][j] = table[i - 1][j] or add_item
    res: Set[int] = set()
    i = n  # start from the last item (last row)
    j = capacity
    while i > 0 and j > 0:
        col = []
        for k in range(i + 1):  # take the column up to the ith item
            col.append(table[k][j])
        i = argmax(col)
        if table[i][j]:  # pick this item
            w = w_list[i - 1]
            res.add(w)
            j -= w
            i -= 1
    return res
