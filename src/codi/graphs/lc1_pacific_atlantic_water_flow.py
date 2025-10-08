"""
LeetCode Logo
Problem List

Dynamic Layout
Premium
0

avatar
417. Pacific Atlantic Water Flow https://leetcode.com/problems/pacific-atlantic-water-flow/description/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain,
and the rain water can flow to neighboring cells directly north, south, east, and west
if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where
result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
"""

from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def bfs(q: Deque) -> Set[Tuple[int, int]]:
            res = set()
            while len(q) != 0:
                i, j = q.popleft()
                res.add((i, j))
                for di, dj in directions:
                    a, b = i + di, j + dj
                    if (
                        0 <= a < rows
                        and 0 <= b < cols
                        and (a, b) not in res
                        and heights[a][b] >= heights[i][j]
                    ):
                        q.append((a, b))
            return res

        q: Deque = deque()
        for i in range(rows):
            q.append((i, 0))
        for j in range(cols):
            q.append((0, j))
        pacific = bfs(q)
        q = deque()
        for i in range(rows):
            q.append((i, cols - 1))
        for j in range(cols):
            q.append((rows - 1, j))
        atlantic = bfs(q)
        return [list(x) for x in pacific & atlantic]
