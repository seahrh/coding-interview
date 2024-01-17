"""
542. 01 Matrix https://leetcode.com/problems/01-matrix/description/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

SOLUTION
Start BFS from zeroes
References
- https://leetcode.com/problems/01-matrix/solutions/3922523/easiest-solution/
"""
from collections import deque
from typing import Deque, List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        mx = rows * cols
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q: Deque = deque()
        # BFS: Initialize queue with all 0s and set cells with 1s to MAX_VALUE.
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = mx
        while len(q) != 0:
            i, j = q.popleft()
            for di, dj in directions:
                a, b = i + di, j + dj
                if 0 <= a < rows and 0 <= b < cols and mat[a][b] > mat[i][j] + 1:
                    q.append((a, b))
                    mat[a][b] = mat[i][j] + 1
        return mat
