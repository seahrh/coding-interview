"""
You are given a list of n integers, and your task is to calculate the number of distinct values in the list.
Input
The first input line has an integer n: the number of values.
The second line has n integers x1,x2,…,xn.

Output
Print one integers: the number of distinct values.

Constraints
1 <= n <= 2·10^5
1 <= xi <= 10^9
Example
Input:
5
2 3 2 2 3

Output:
2

See https://cses.fi/problemset/task/1621
SOLUTION
Sort the array in-place, then increment count when a different value is seen.
Time O(N lg N)
Space O(1)
"""
from typing import List


def count_distinct(arr: List[int]) -> int:
    arr.sort()
    res = 0 if len(arr) == 0 else 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            res += 1
    return res
