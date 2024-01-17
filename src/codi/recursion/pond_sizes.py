"""
Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location
represents the height above sea level. A value of zero indicates water. A pond is a region of water
connected vertically, horizontally, or diagonally. The size of the pond is the total number of
connected water cells. Write a method to compute the sizes of all ponds in the matrix.
EXAMPLE
Input:
0 2 1 0
0 1 0 1
1 1 0 1
0 1 0 1
Output: 2, 4, 1 (in any order)

(16.19, p515)
"""


def _pond_size(land, i, j):
    # check index out of bounds and base case: no water here or cell is visited
    if i < 0 or j < 0 or i >= len(land) or j >= len(land[0]) or land[i][j] != 0:
        return 0
    size = 1
    land[i][j] = -1  # mark visited
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            size += _pond_size(
                land, i + di, j + dj
            )  # O(mn) space if all cells have water
    return size


def pond_sizes(land):
    """Modified depth-first search. To avoid recounting cells, mark the cell as visited.
    O(mn) time and O(mn) space, where m is number of rows and n is number of columns."""
    res = []
    if len(land) == 0 or len(land[0]) == 0:
        return res
    rows = len(land)
    cols = len(land[0])
    for i in range(rows):
        for j in range(cols):
            if land[i][j] == 0:
                size = _pond_size(land, i, j)
                res.append(size)
    return res
