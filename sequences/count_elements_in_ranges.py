"""
Given an array of numbers and an array of pairs denoting ranges (ends inclusive),
count the numbers that appear in the ranges. Nums do not contain duplicates.

example:
nums: [4, 2, 11]
ranges: [[2,4], [5,6], [7,9]]
result = 2 (2 and 4)
"""


def count(nums, ranges):
    """Build a set from ranges, then loop nums to increment counter.
    Time O(n + p)"""
    if len(nums) == 0:
        raise ValueError('nums must not be empty')
    if len(ranges) == 0:
        raise ValueError('ranges must not be empty')
    s = set()
    for r in ranges:  # O(p)
        s.update(range(r[0], r[1] + 1))
    res = 0
    for n in nums:  # O(n)
        if n in s:
            res += 1
    return res
