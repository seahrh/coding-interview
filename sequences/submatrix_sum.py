"""
Max Submatrix: Given an NxN matrix of positive and negative integers, write code to find the
submatrix with the largest possible sum.

(17.24, p623)
SOLUTION
For each row, find the contiguous sequence of columns that give the max sum.
Between the top edge (row) and bottom edge (row) of the submatrix,
sum the values column-wise. This gives a 1D array to find max subsequence sum
in O(n) time.

Let R be number of rows and C be number of columns of the matrix.
O(R^2C) time
O(C) space: store the cumulative column sums
"""
from collections import namedtuple
import sys


Cell = namedtuple('Cell', 'row col')

Range = namedtuple('Range', 'lo hi sum')

Submatrix = namedtuple('Submatrix', 'top_left bottom_right sum')


def _max_subarray(arr):
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    _max = -sys.maxsize
    _sum = 0
    lo = 0
    best = None
    for i in range(len(arr)):
        _sum += arr[i]
        if _sum > _max:
            _max = _sum
            best = Range(lo=lo, hi=i, sum=_max)
            continue
        if _sum < 0:
            _sum = 0
            if i + 1 < len(arr):
                lo = i + 1
    return best


def max_submatrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError('matrix must not be empty')
    rows = len(matrix)
    cols = len(matrix[0])
    best = None
    for trow in range(rows):  # top row O(R^2C) time
        cumulative_col_sum = [0] * cols
        for brow in range(trow, rows):  # bottom row O(RC) time
            for col in range(cols):  # O(C) time
                # adds up column-wise, collapses into a single row!
                cumulative_col_sum[col] += matrix[brow][col]
            best_range = _max_subarray(cumulative_col_sum)  # O(C) time
            if best is None or best.sum < best_range.sum:
                best = Submatrix(
                    top_left=Cell(row=trow, col=best_range.lo),
                    bottom_right=Cell(row=brow, col=best_range.hi),
                    sum=best_range.sum
                )
    return best
