"""
=============================
Recover Matrix From Checksum
=============================
There is a board with 2 rows and N columns, represented by a matrix M.
Rows are numbered from 0 to 1 from top to bottom
and columns are numbered from 0 to N-1 from left to right.
Each cell contains either a 0 or a 1.

Rules
- sum of integers in 0th (upper) row equals U
- sum of integers in 1st (lower) row equals L
- sum of integers in Kth columns equals C[K]
- each element of array C is an integer in the range [0, 2]

Given two integers U and L and an array C of N integers, recover M.
Return M as a single string in the format "UPPER,LOWER"
where UPPER and LOWER are strings containing the digits '0' or '1'.
If multiple solutions exist, return any one of them.
If no solution exists, return "IMPOSSIBLE".

SOLUTION: Backtracking
Fill one column at a time, going from left to right.
At each step, prune if column sum is not satisfied.
Evaluate row sums after all columns have been filled.

Time O(4^N) ~= O(2^N): four-way split at each level of the recursion tree.
Space O(N): recursive call stack
"""
from typing import List


_DEFAULT: int = -999


def _equals_column_sum(
    column_sum: List[int], column: int, partial: List[List[int]]
) -> bool:
    return column_sum[column] == partial[0][column] + partial[1][column]


def _recover_matrix(
    upper_sum: int,
    lower_sum: int,
    column_sum: List[int],
    column: int,
    partial: List[List[int]],
) -> bool:
    # base case: all columns filled, ready to evaluate row sums.
    if column == len(column_sum):
        if upper_sum != sum(partial[0]):
            return False
        if lower_sum != sum(partial[1]):
            return False
        return True
    partial[0][column] = 0
    partial[1][column] = 0
    if _equals_column_sum(column_sum, column, partial) and _recover_matrix(
        upper_sum, lower_sum, column_sum, column + 1, partial
    ):
        return True
    partial[0][column] = 0
    partial[1][column] = 1
    if _equals_column_sum(column_sum, column, partial) and _recover_matrix(
        upper_sum, lower_sum, column_sum, column + 1, partial
    ):
        return True
    partial[0][column] = 1
    partial[1][column] = 0
    if _equals_column_sum(column_sum, column, partial) and _recover_matrix(
        upper_sum, lower_sum, column_sum, column + 1, partial
    ):
        return True
    partial[0][column] = 1
    partial[1][column] = 1
    if _equals_column_sum(column_sum, column, partial) and _recover_matrix(
        upper_sum, lower_sum, column_sum, column + 1, partial
    ):
        return True
    return False


def recover_matrix(upper_sum: int, lower_sum: int, column_sum: List[int]) -> str:
    partial: List[List[int]] = [[_DEFAULT] * len(column_sum) for _ in range(2)]
    # print(repr(partial))
    if _recover_matrix(upper_sum, lower_sum, column_sum, 0, partial):
        first = "".join([str(x) for x in partial[0]])
        second = "".join([str(x) for x in partial[1]])
        return ",".join([first, second])
    return "IMPOSSIBLE"
