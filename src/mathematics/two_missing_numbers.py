"""
Given an unsorted array of n unique integers where each element in the array is in range [1, n].
The array has all distinct elements and size of array is (n-2).
Hence Two numbers from the range are missing from this array.
Find the two missing numbers. We are looking for a solution that takes O(N) time and O(1) space.

SOLUTION
arrSum is the Sum of all elements in the array
Sum of 2 missing numbers = (Sum of integers from 1 to n) - arrSum
Average of 2 missing numbers = sum of missing numbers / 2
One of the numbers will be less than or equal to avg while the other one will be strictly greater then avg.
Two numbers can never be equal since all the given numbers are distinct.
Potential issues: integer overflow
Time O(N)
Space O(1)

See https://www.geeksforgeeks.org/find-two-missing-numbers-set-1-an-interesting-linear-time-solution/
"""
from typing import List, Tuple


def solve(n: int, arr: List[int]) -> Tuple[int, int]:
    expected = int(n * (n + 1) / 2)
    missing_sum = expected - sum(arr)
    avg: int = int(missing_sum / 2)
    expected = int(avg * (avg + 1) / 2)
    actual = 0
    for a in arr:
        if a <= avg:
            actual += a
    first: int = expected - actual
    second: int = missing_sum - first
    if first < second:
        return first, second
    return second, first
