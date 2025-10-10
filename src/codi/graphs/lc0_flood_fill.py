"""
733. Flood Fill https://leetcode.com/problems/flood-fill/description/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

SOLUTION
Time O(MN)
Each cell (i, j) in the grid is visited at most once:
The DFS visits up to 4 neighbors per cell (constant factor).
So, total work is proportional to the number of pixels in the image.

Space O(MN)
There are two sources of space usage:
Visited matrix: O(m × n)
Recursion stack: in the worst case, all cells are part of the same region → recursion depth = O(m × n)
If you removed visited and directly checked color changes instead,
you could reduce extra space to just the recursion stack.
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])
        visited = [[0] * n for _ in range(m)]
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ori = image[sr][sc]

        def dfs(i: int, j: int) -> None:
            if visited[i][j] == 1:
                return
            visited[i][j] = 1
            if image[i][j] == ori:
                image[i][j] = color
            for d in directions:
                a, b = i + d[0], j + d[1]
                if 0 <= a < m and 0 <= b < n and image[a][b] == ori:
                    dfs(a, b)

        dfs(sr, sc)
        return image
