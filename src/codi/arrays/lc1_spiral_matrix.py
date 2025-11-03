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
1. Define the matrix’s boundaries:
- top (r1), bottom (r2)
- left (c1), right (c2)
2. Iteratively visit the four borders:
- Top row (left to right)
- Right column (top + 1 to bottom)
- Bottom row (right - 1 to left), if there’s more than one row
- Left column (bottom - 1 to top + 1), if there’s more than one column
3. Move boundaries inward and repeat until all cells are visited.

Boundaries (r1, r2, c1, c2) shrink inward to process each “layer” of the spiral.
On each pass:
We add the top row, right column, (if any) bottom row, (if any) left column.
The checks (if r1 < r2, if c1 < c2) prevent double visiting rows or columns
when the spiral gets down to a single line.
Time complexity: O(MN) — every element is visited exactly once.
Space complexity: O(1) excluding the output list.

The solution doesn’t use recursion; it’s iterative for efficiency and low stack use.
Boundary checks make it resilient for non-square and small matrices.
No extra matrix copy, space-optimal except for result.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            # Top row
            for c in range(c1, c2 + 1):
                res.append(matrix[r1][c])
            # Right column
            for r in range(r1 + 1, r2 + 1):
                res.append(matrix[r][c2])
            # Bottom row (if not same as top)
            if r1 < r2:
                for c in range(c2 - 1, c1 - 1, -1):
                    res.append(matrix[r2][c])
            # Left column (if not same as right)
            if c1 < c2:
                for r in range(r2 - 1, r1, -1):
                    res.append(matrix[r][c1])
            # Move inward
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res
