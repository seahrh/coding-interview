"""
Majority Element: A majority element is an element that makes up more than half of the items in
an array. Given an array of integers including zero, positive and negative integers,
find the majority element.
If there is no majority element, return None.
Do this in O(N) time and O(1) space.
Input: 1 2 5 9 5 9 5 5 5
Output: 5

(17.10, p565)
SOLUTION
If the majority item appears less at the beginning, it must appear more often at the end.
To find the candidate in one pass, if we miss it at the beginning, we will pick it up towards the end.
Run in two passes: first to find the majority candidate and validate that it is indeed majority.
"""
from typing import List, Optional


def _candidate(arr: List[int]) -> int:
    res: int = -1
    count = 0
    for a in arr:
        if count == 0:
            res = a
        if res == a:
            count += 1
        else:
            count -= 1
    return res


def _is_majority(arr: List[int], candidate: int) -> bool:
    count = 0
    for a in arr:
        if a == candidate:
            count += 1
    return count > int(len(arr) / 2)


def majority_element(arr: List[int]) -> Optional[int]:
    c = _candidate(arr)
    if _is_majority(arr, c):
        return c
    return None
