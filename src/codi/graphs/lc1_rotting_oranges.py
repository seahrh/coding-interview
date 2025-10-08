"""
994. Rotting Oranges https://leetcode.com/problems/rotting-oranges/description/

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, mins = 0, 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q: Deque = deque()
        # BFS: Initialize queue with rotting oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, mins))
                    continue
                if grid[i][j] == 1:
                    fresh += 1
        while len(q) != 0:
            i, j, mins = q.popleft()
            for di, dj in directions:
                a, b = i + di, j + dj
                if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 1:
                    q.append((a, b, mins + 1))
                    grid[a][b] = 2
                    fresh -= 1
        if fresh != 0:
            mins = -1
        return mins  # minutes elapsed for the last dequeued rotting orange
