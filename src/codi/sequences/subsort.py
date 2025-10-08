"""
Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted
elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest
such sequence).
EXAMPLE
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9)

(16.16, p507)
"""

import sys


def _last_index_of_left_partition(arr):
    """Longest non-decreasing subsequence"""
    prev = -sys.maxsize
    for i in range(len(arr)):
        if arr[i] < prev:
            return i - 1
        prev = arr[i]
    return len(arr) - 1


def _first_index_of_right_partition(arr):
    """Longest non-increasing subsequence"""
    prev = sys.maxsize
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > prev:
            return i + 1
        prev = arr[i]
    return 0


def subsort(arr):
    """Partition the array into three regions such that left < middle < right.
    Left partition: longest non-decreasing subsequence
    Right partition: longest non-increasing subsequence (from right to left)
    Find the min and max of the middle region.
    Shrink left and right partitions until left < middle < right.
    O(n) time and O(1) space."""
    if len(arr) == 0:
        raise ValueError("arr must not be empty")
    tail = len(arr) - 1
    left_hi = _last_index_of_left_partition(arr)
    if left_hi == tail:  # array already sorted
        return None
    right_lo = _first_index_of_right_partition(arr)
    max_index = left_hi
    min_index = right_lo
    # get min and max of the middle region
    for i in range(left_hi + 1, right_lo):
        if arr[i] < arr[min_index]:
            min_index = i
        if arr[i] > arr[max_index]:
            max_index = i
    # shrink left until less than or equals min
    _min = arr[min_index]
    lo = left_hi
    while lo >= 0:
        if arr[lo] <= _min:
            break
        lo -= 1
    lo += 1
    _max = arr[max_index]
    # shrink right until greater than or equals max
    hi = right_lo
    while hi <= tail:
        if arr[hi] >= _max:
            break
        hi += 1
    hi -= 1
    return lo, hi
