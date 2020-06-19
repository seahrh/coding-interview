"""
Subset Sum
=============
Given a SET of non-negative integers, and a value sum C, find all subsets with sum equal to C.
Variant of 0/1 Knapsack problem where all items have the same value per unit weight.

SOLUTION: Backtracking
Time O(2^N)
Space O(N): recursive call stack

Based on https://www.youtube.com/watch?v=kyLxTdsT8ws
"""
from typing import Set, FrozenSet, List


def _subset_sum(
    capacity: int,
    weights: List[int],
    index: int,
    partial: Set[int],
    result: Set[FrozenSet[int]],
) -> None:
    _sum = sum(partial)
    if _sum == capacity:
        result.add(frozenset(partial))
        return
    if _sum > capacity:
        return
    # check last because last item could be in the solution
    if index >= len(weights):
        return
    partial.add(weights[index])
    _subset_sum(capacity, weights, index + 1, partial, result)
    partial.remove(weights[index])
    _subset_sum(capacity, weights, index + 1, partial, result)


def subset_sum(capacity: int, weights: Set[int]) -> Set[FrozenSet[int]]:
    if capacity < 1:
        raise ValueError("Capacity must be at least 1")
    res: Set[FrozenSet[int]] = set()
    _subset_sum(capacity, weights=list(weights), index=0, partial=set(), result=res)
    return res
