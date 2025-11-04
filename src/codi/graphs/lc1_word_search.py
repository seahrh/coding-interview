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

SOLUTION
Search pruning means stopping the search as soon as it's clear that no valid solution can be found down a particular path.
In the context of word search, it helps avoid exploring unnecessary paths, saving time.

High-Level Approach
Use DFS (depth-first search) to try to build the word starting from each cell.
Only consider cells that match the correct character at that step.
Mark cells as visited to prevent reusing them.
Pruning Mechanisms in the Solution
Character mismatch: If current cell doesn't match word[k], stop immediately — don't explore further from here.
Out of bounds: If the cell is out of bounds, prune the search.
Visited Cell: Use an in-place mark (temporarily set the cell to '#') so the DFS won't revisit the same cell during one path.
Early exit: As soon as all characters match (i.e., we reach k == len(word) - 1), return True.
Early character count pruning:
Before starting the DFS, count the required characters in word and what's available in the board.
If the board doesn't have enough of any required character, skip DFS entirely.

Why Is This Efficient?
Avoids unnecessary paths: DFS only follows paths that match the next letter of word.
Early escapes: If a path can't possibly match the word, don't explore neighbors further.
No extra space for visited grid: In-place marking saves memory.
Quick rejection for impossible cases: Character count pre-check can save huge effort for long or impossible words.

Time O(MN * 4^L), where L is the word length
Each cell in the board can be a starting point.
For each starting cell, you potentially search up to four directions at every step (but never revisit the same cell).
Each path can visit up to word.length cells.
From each cell, at each position in the word, you branch to up to 4 directions (except blocked/visited cells).

Space O(L): Only recursion stack and temporary marking for visited cells are used (no extra grid).
"""

from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # Prune invalid position and character mismatch
            if not (0 <= i < m and 0 <= j < n):
                return False
            if board[i][j] != word[k]:
                return False
            # Found all characters in the word
            if k == len(word) - 1:
                return True
            # Prune: check if the current cell is already visited using in-place marking
            tmp = board[i][j]
            board[i][j] = "#"  # Mark as visited
            # Explore neighbors
            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )
            board[i][j] = tmp  # Unmark (restore original value)
            return found

        # Optimization: Early pruning based on character counts
        word_count = Counter(word)
        board_count = Counter(c for row in board for c in row)
        for c in word_count:
            if word_count[c] > board_count[c]:
                return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
