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


def _candidate(arr):
    res = -1
    count = 0
    for v in arr:
        if count == 0:
            res = v
        if res == v:
            count += 1
        else:
            count -= 1
    return res


def _validate(arr, candidate):
    count = 0
    for v in arr:
        if v == candidate:
            count += 1
    return count > int(len(arr) / 2)


def majority_element(arr):
    c = _candidate(arr)
    if _validate(arr, c):
        return c
    return None
