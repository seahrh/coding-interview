"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

You are allowed to modify the array in-place.

SOLUTION
Sort the array and run through all indices of a possible first element of a triplet.
For each possible first element, make a bi-directional sweep of the remaining part of the array.

Time O(N^2)
Space O(1)
"""
from typing import List, NamedTuple, Set


class Triple(NamedTuple):
    i: int
    j: int
    k: int


def three_sum(arr: List[int]) -> Set[Triple]:
    res: Set[Triple] = set()
    arr.sort()  # in-place sort
    for i in range(len(arr) - 2):  # maintain two slots ahead for j, k
        j = i + 1
        k = len(arr) - 1
        while j < k:
            _sum = arr[i] + arr[j] + arr[k]
            if _sum == 0:
                res.add(Triple(arr[i], arr[j], arr[k]))
                j += 1
                k -= 1
                continue
            if _sum < 0:
                j += 1
                continue
            k -= 1
    return res
