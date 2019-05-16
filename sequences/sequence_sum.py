import sys

# You are given an array of integers (both positive and negative). Find the
# continuous sequence with the largest sum. Return the sum. [CTCI Q19.7]
#
# EXAMPLE Input: {2, -8, 3, -2, 4, -10}
# Output: 5 (i.e., {3, -2, 4} )
#
# Assume subsequence cannot be empty if the array contains all negative integers.


def largest_sum(arr):
    # If sum drops below zero, that subsequence will not contribute to the maximal subsequence
    # since max is reduced by adding the negative sum.
    # If the array contains all negative numbers, sum is reset for each element,
    # effectively picking the smallest negative number.
    # This takes O(n) time and O(1) space.
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    _max = -sys.maxsize
    _sum = 0
    for i in arr:
        _sum += i
        if _sum > _max:
            _max = _sum
        elif _sum < 0:
            _sum = 0
    return _max
