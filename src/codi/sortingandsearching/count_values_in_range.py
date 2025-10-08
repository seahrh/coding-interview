"""
Queries for counts of array elements with values in given range
Given an unsorted array of size n, find no of elements between two elements i and j (both inclusive).

Examples:

Input :  arr = [1 3 3 9 10 4]
         i1 = 1, j1 = 4
         i2 = 9, j2 = 12
Output : 4
         2
The numbers are: 1 3 3 4 for first query
The numbers are: 9 10 for second query

SOLUTION
An Efficient Approach will be to first sort the array,
then using a modified binary search function find two indices,
one of first element >= lower bound of range
and the other of the last element <= upperbound.

Time O(N lg N): Each query takes O(lg N) time, sorting takes O(N lg N) time.
Space O(1)

See https://www.geeksforgeeks.org/queries-counts-array-elements-values-given-range/
"""

from typing import List


def lower_index(arr: List[int], lower: int) -> int:
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo / 2 + hi / 2)
        if arr[mid] < lower:
            lo = mid + 1
            continue
        hi = mid - 1
    return lo


def upper_index(arr: List[int], upper: int) -> int:
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo / 2 + hi / 2)
        if arr[mid] > upper:
            hi = mid - 1
            continue
        lo = mid + 1
    return hi


def count(arr: List[int], lower: int, upper: int) -> int:
    if len(arr) == 0:
        raise ValueError("array must not be empty")
    if upper < lower:
        raise ValueError("lower bound must be less than or equal to the upper bound")
    arr.sort()
    # add one because the lower index is included as well
    return upper_index(arr, upper) - lower_index(arr, lower) + 1
