"""
Given an array of n integers, find 3 elements such that a[i] < a[j] < a[k] and i < j < k in O(n) time.
Return the indices i, j and k if the triple exists, else return None.
Find one such solution, not all solutions.

SOLUTION
Single pass O(N) time solution based on https://stackoverflow.com/a/33982388/519951
"""

from typing import List, Optional, Tuple


def increasing_triple(arr: List[int]) -> Optional[Tuple[int, int, int]]:
    if len(arr) < 3:
        return None
    _min = 0
    lo = 0
    mid = 0
    has_candidates = False
    for i in range(1, len(arr)):
        if arr[i] < arr[_min]:
            _min = i
            continue
        if arr[i] == arr[_min]:
            continue
        # If candidates are present, reset the solution when
        # current element is greater than the minimum seen so far but not greater than mid.
        if not has_candidates or arr[i] <= arr[mid]:
            lo = _min
            mid = i
            has_candidates = True
            continue
        # have candidates and current element is greater than mid
        return lo, mid, i
    return None
