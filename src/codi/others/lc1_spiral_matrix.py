"""
54. Spiral Matrix https://leetcode.com/problems/spiral-matrix/description/

Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

SOLUTION
Recursively visit the 4 borders of the matrix.
Set the topLeft and bottomRight corners of the inner matrix.
Consider corner cases where the inner matrix is only one row or one column.
Time O(MN)
Space O(1)
"""
from typing import List


class Solution:
    def borders(
        self, matrix: List[List[int]], r1: int, c1: int, r2: int, c2: int
    ) -> List[int]:
        res = []
        for i in range(c1, c2 + 1):
            print(f"top m[{r1}][{i}]")
            res.append(matrix[r1][i])
            print(res)
        for i in range(r1 + 1, r2 + 1):
            print(f"right m[{i}][{c2}]")
            res.append(matrix[i][c2])
            print(res)
        if r1 < r2:
            for i in range(c2 - 1, c1 - 1, -1):
                print(f"bottom m[{r2}][{i}]")
                res.append(matrix[r2][i])
                print(res)
        if c1 < c2:
            for i in range(r2 - 1, r1, -1):
                print(f"left m[{i}][{c1}]")
                res.append(matrix[i][c1])
                print(res)
        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        r1, c1 = 0, 0
        r2, c2 = len(matrix) - 1, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            res += self.borders(matrix, r1, c1, r2, c2)
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return res
