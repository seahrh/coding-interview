"""
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (absolute) difference. Return the difference.
(16.6, p485)
"""
import sys


def smallest_difference(a, b):
    """Return the smallest absolute difference between any pairs in two arrays of numbers.
    First, sort the arrays then search for the pair.
    Idea: Advancing the pointer to the larger value only makes the difference larger,
    so advance the smaller value instead.
    This takes O(A log A + B log B) time to sort and O(A + B) time to find smallest difference.
    Thus overall runtime is 0 (A log A + B log B) and O(1) space.
    """
    if len(a) == 0:
        raise ValueError("array a must not be empty")
    if len(b) == 0:
        raise ValueError("array b must not be empty")
    a.sort()  # sort in-place
    b.sort()
    i = 0
    j = 0
    _min = sys.maxsize
    while i < len(a) and j < len(b):  # O(A + B) time
        diff = abs(a[i] - b[j])
        if diff < _min:
            _min = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return _min
