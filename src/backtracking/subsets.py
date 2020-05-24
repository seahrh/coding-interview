"""
Implement an efficient algorithm for listing all k-element subsets of n items.
Input array does not contain duplicates.

SOLUTION
Time O(N! / K!)
"""
from typing import Set, List, FrozenSet


def _subsets(arr: List[int], k: int, partial: FrozenSet[int]) -> Set[FrozenSet[int]]:
    if len(partial) == k:  # base case
        return {partial}
    res: Set[FrozenSet[int]] = set()
    for a in arr:  # DFS
        if a in partial:  # pruning: do not extend the partial solution
            continue
        res = res | _subsets(arr, k, partial | {a})
    return res


def subsets(arr: List[int], k: int) -> Set[FrozenSet[int]]:
    if k > len(arr):
        raise ValueError("k must not exceed array length")
    return _subsets(arr, k, partial=frozenset())
