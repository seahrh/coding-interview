"""
You are given an array of integers (both positive and negative). Find the
continuous sequence with the largest sum. Return the sum. [CTCI Q19.7]

EXAMPLE Input: {2, -8, 3, -2, 4, -10}
Output: 5 (i.e., {3, -2, 4} )

Assume subsequence cannot be empty if the array contains all negative integers.
"""
import sys


def largest_sum(arr):
    """If sum drops below zero, that subsequence will not contribute to the maximal subsequence
    since max is reduced by adding the negative sum.
    If the array contains all negative numbers, sum is reset for each element,
    effectively picking the smallest negative number.
    This takes O(n) time and O(1) space."""
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


# Question: Given a sequence of positive integers A and an integer T,
# return whether there is a *continuous sequence* of A that sums up to exactly T.
# Example [23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20
# [1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8
# [1, 3, 5, 23, 2], 7 Return False because no sequence in this array adds up to 7
#
# Note: We are looking for an O(N) solution. There is an obvious O(N^2)
# solution which is a good starting point but is not the final solution we are looking for.


def sequence_sum_equals(arr, target):
    """Keep growing the window to the right until sum exceeds target.
    Then shrink the window from the left, checking for target at each step.
    Solution based on @url https://www.careercup.com/question?id=6305076727513088
    This takes O(n) time and O(1) space.
    """
    if target < 1:
        raise ValueError('target must be a positive number')
    _sum = 0
    lo = 0  # beginning index of the window
    for v in arr:
        _sum += v
        if _sum == target:
            return True
        while _sum > target:
            _sum -= arr[lo]
            if _sum == target:
                return True
            lo += 1
    return False
