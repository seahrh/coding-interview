"""
Implement an efficient algorithm for listing all k-element subsets of n items.
Input array does not contain duplicates.

SOLUTION
Time O(2^N)
Space O(N): depth of recursive call stack
"""

from typing import FrozenSet, List, Set


def _solve(
    arr: List[int], k: int, index: int, partial: Set[int], result: Set[FrozenSet[int]]
) -> None:
    if len(partial) == k:  # complete solution
        result.add(frozenset(partial))
        return
    if index == len(arr):  # terminate recursion
        return
    partial.add(arr[index])
    _solve(arr, k, index=index + 1, partial=partial, result=result)
    partial.remove(arr[index])
    _solve(arr, k, index=index + 1, partial=partial, result=result)


def solve(arr: List[int], k: int) -> Set[FrozenSet[int]]:
    if k > len(arr):
        raise ValueError("k must not exceed array length")
    res: Set[FrozenSet[int]] = set()
    _solve(arr, k, index=0, partial=set(), result=res)
    return res
