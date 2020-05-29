"""
Shortest Winter
=====================
Divide the year into winter and summer. Winter comes before summer and each winter's temperature
measurement is smaller than any temperature measured in summer.
Given an array of daily temperature measurements, find a partition such that winter is shortest
and return the length of winter. Each of winter and summer must be at least one day long.

SOLUTION
- Partitions must satisfy: max(left) < min(right)
- get min(right) with a single pass through the array, loop from right to left.

Time O(N)
Space O(N)
"""
from typing import List


def length(arr: List[int]) -> int:
    """Returns the length of the left partition (winter)."""
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")
    min_right: List[int] = [arr[-1]] * len(arr)
    # loop from right to left; starting with the 2nd last element
    for i in range(len(arr) - 2, -1, -1):
        min_right[i] = min(arr[i], min_right[i + 1])
    _max = arr[0]
    # loop until 2nd last element because size of right partition is at least 1
    for i in range(len(arr) - 1):
        _max = max(arr[i], _max)
        if i + 1 < len(arr) and _max < min_right[i + 1]:
            return i + 1
    return len(arr) - 1  # longest winter
