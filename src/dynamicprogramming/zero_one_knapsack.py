"""
0/1 Knapsack Problem
======================
Given weights and values of N items, put these items in a knapsack of capacity C
to get the maximum total value in the knapsack.
You cannot divide an item, either pick the whole item or don’t pick it (0-1 property).
Return a boolean array that indicates whether the item is present in the knapsack.

If multiple solutions exist, just return any one of them.

SOLUTION
Dynamic programming (tabulation)
Time O(NC)
Space O(NC)

Based on https://www.youtube.com/watch?v=nLmhmB6NzcM
"""
from typing import List
from util import argmax


def knapsack(capacity: int, weights: List[int], values: List[int]) -> List[bool]:
    if len(weights) == 0:
        raise ValueError("Weights array must not be empty")
    if len(values) == 0:
        raise ValueError("Values array must not be empty")
    if len(weights) != len(values):
        raise ValueError("Both weights and values arrays must have equal length")
    n = len(weights)
    table: List[List[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            item = i - 1
            remainder = j - weights[item]
            add_item = 0
            if remainder >= 0:
                add_item = table[i - 1][remainder] + values[item]
            # decide whether to add item or not
            table[i][j] = max(table[i - 1][j], add_item)
    res: List[bool] = [False] * n
    i = n  # start from the last item (last row)
    j = capacity
    while i > 0 and j > 0:
        col = []
        for k in range(i + 1):  # take the column up to the ith item
            col.append(table[k][j])
        i = argmax(col)
        if table[i][j] != 0:  # pick this item because it increased the total value
            item = i - 1
            res[item] = True
            j -= weights[item]
            i -= 1
    return res
