"""
74. Search a 2D Matrix https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4

SOLUTION
Binary search in 2 steps
1. Find which row contains the target. Let the 1st element of each row represent that row.
2. Search the row containing target
Time O(lg M + lg N) = O(lg MN) by laws of logarithm
Space O(1)
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1  # number of rows
        i = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                i = mid
                lo = mid + 1
                continue
            hi = mid - 1
        lo = 0
        hi = len(matrix[i]) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[i][mid] == target:
                return True
            if matrix[i][mid] < target:
                lo = mid + 1
                continue
            hi = mid - 1
        return False
