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
What’s the Problem?
For each cell in a binary matrix (mat), find the distance to the nearest zero (0).
Adjacent cell moves (up/down/left/right) cost 1.
Solution Approach: Multi-source Breadth-First Search (BFS)
Instead of searching from every cell with a 1 (which would be slow),
we start BFS from all cells containing 0.
This way, each cell’s answer is found as soon as it’s reached for the first time by BFS.

Key Insights
Multi-source BFS:
By processing all zeroes first, every cell’s shortest path is naturally discovered in waves—cells closest to zeroes get filled first.
In-place Update:
The matrix mat is reused to store results—saves space.
Efficient Search:
Each cell is processed at most once. No wasted work.
Time & Space Complexity
Time: O(m × n). Each cell is enqueued and processed once.
Space: O(m × n). For the queue at worst, plus the matrix itself.

References
- https://leetcode.com/problems/01-matrix/solutions/3922523/easiest-solution/
"""

from collections import deque
from typing import Deque, List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        mx = m * n
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # Create a queue.
        # For every cell, if it's a zero, add its position to the queue.
        # If it's a 1, set its value to a big number to mark it as not yet reached.
        q: Deque = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = mx
        # BFS while the queue isn't empty:
        # pop a cell position (i, j)
        # For each direction (up, down, left, right), check adjacent cell (a, b)
        # If the neighbor hasn’t been reached by a shorter route (mat[a][b] > mat[i][j] + 1):
        # Update its value (mat[a][b] = mat[i][j] + 1).
        # Add it to the queue—its neighbors now get updated next.
        while len(q) != 0:
            i, j = q.popleft()
            for di, dj in directions:
                a, b = i + di, j + dj
                if 0 <= a < m and 0 <= b < n and mat[a][b] > mat[i][j] + 1:
                    q.append((a, b))
                    mat[a][b] = mat[i][j] + 1
        return mat
