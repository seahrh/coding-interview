"""
79. Word Search https://leetcode.com/problems/word-search/description/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        vis: List[List[int]] = [[0] * n for _ in range(m)]

        def dfs(board: List[List[str]], word: str, i: int, j: int, k: int) -> bool:
            nonlocal vis
            if k == len(word) - 1 and board[i][j] == word[k]:
                return True
            if board[i][j] != word[k]:
                return False
            vis[i][j] = 1
            for d in directions:
                a, b = i + d[0], j + d[1]
                if 0 <= a < m and 0 <= b < n:
                    if vis[a][b] == 1:
                        continue
                    if dfs(board, word, a, b, k + 1):
                        return True
            vis[i][j] = 0  # release the node so that it can be reused!
            return False

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(board, word, i, j, k=0):
                    return True
        return False
