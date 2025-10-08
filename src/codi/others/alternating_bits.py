"""
Given a binary string, that is it contains only 0s and 1s.
We need to make this string a sequence of alternate characters by flipping some of the bits,
our goal is to minimize the number of bits to be flipped.

Examples :
Input : str = “001”
Output : 1
Minimum number of flips required = 1
We can flip 1st bit from 0 to 1

Input : str = “0001010111”
Output : 2
Minimum number of flips required = 2
We can flip 2nd bit from 0 to 1 and 9th
bit from 1 to 0 to make alternate
string “0101010101”.
Expected time complexity : O(n) where n is length of input string.

See https://www.geeksforgeeks.org/number-flips-make-binary-string-alternate/
"""

from typing import List


def _flips(arr: List[int], begin: int) -> int:
    res = 0
    expected = begin
    for a in arr:
        if a != expected:
            res += 1
        expected = 1 - expected
    return res


def min_flips(arr: List[int]) -> int:
    """Time O(N)
    Space O(1)
    """
    return min(_flips(arr, begin=0), _flips(arr, begin=1))
