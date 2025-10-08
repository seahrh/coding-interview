"""
73. Set Matrix Zeroes https://leetcode.com/problems/set-matrix-zeroes/description/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

SOLUTION
Use the first row to mark the columns that should be set zero.
Use the first column to mark the rows that should be set zero.
Time O(MN)
Space O(1)
References
- https://leetcode.com/problems/set-matrix-zeroes/solutions/3472518/full-explanation-super-easy-constant-space/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row, first_col = False, False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # processing the rest of the matrix[1:][1:] depends on 1st row and 1st col,
        # so do not modify 1st row and 1st col at this point
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
