"""
Images are stored in the form of a grid.
Image recognition is possible by comparing grids of two images and checking if they have any matching regions.
You are given two grids where each cell of a grid contains is either 0 or 1.
If two cells share a side then they are adjacent.
Cells that contain 1s form a connected region if any cell of that region can be reached by
moving through the adjacent cells that contain 1.
Overlay the first grid onto the second and
if a region in the first grid completely matches a region in the second grid, the regions are matched.
Count total number of such matched regions in the second grid.
For example given two 3x3 grids:
G1:	111		G2: 111
    100			100
    100			101
There are two regions in G2: {(0,0), (0,1), (0,2), (1,0), (2,0)} and {(2,2)}.
Regions in G1 cover the first region in G2 but not the second region. Thus, there is only one matching region.
Making a slight alteration to the above example:
G1:	111		G2: 111
    101			100
    100			101
Now there are no matching regions.
From G1, "1" at position (1,2) is not matched in G2. G2[2][2] == "1" is not matched in G1.

Complete the function countMatches below. The function must return the number of matching regions.
It has the following parameters:
• G1[G1[0], ..., G1[n-1]]: an array of bit strings representing the rows if image 1
• G2[G2[0], ..., G2[n-1]]: an array of bit strings representing the rows if image 2

Constraints:
▪ 1 ≤ n ≤ 100
▪ 1 ≤ |G1[i]|, |G2[i]| ≤ 100
▪ Grid cells contain only 0 or 1
SOLUTION
Compare the cells in both the grids G1 with G2
- if both 1's, keep as it is
- if both 0's, keep as it is
- if both are different, change the cell to 2;
- count all connected components that do not contain '2'
Time O(N^2): worst case max number of connected components is N^2/2
Space O(N^2): assume original grids cannot be modified, so make own grid to maintain state.
See https://leetcode.com/discuss/interview-question/231726/image-matching
"""

from copy import deepcopy
from typing import List, Set, Tuple


def _is_new_matching_region(g: List[List[int]], i: int, j: int) -> bool:
    """DFS to search for connected component at position (i, j)."""
    st: List[Tuple[int, int]] = [(i, j)]
    discovered: Set[Tuple[int, int]] = {(i, j)}
    while len(st) != 0:
        i, j = st.pop()
        # connected component is either conflicted or visited
        if g[i][j] >= 2:
            return False
        if g[i][j] == 0:
            continue
        curr: Tuple[int, int] = (i - 1, j)
        if i - 1 >= 0 and curr not in discovered:
            discovered.add(curr)
            st.append(curr)
        curr = (i + 1, j)
        if i + 1 < len(g) and curr not in discovered:
            discovered.add(curr)
            st.append(curr)
        curr = (i, j - 1)
        if j - 1 >= 0 and curr not in discovered:
            discovered.add(curr)
            st.append(curr)
        curr = (i, j + 1)
        if j + 1 < len(g[0]) and curr not in discovered:
            discovered.add(curr)
            st.append(curr)
    # mark connected component as visited
    for i, j in discovered:
        if g[i][j] == 1:
            g[i][j] = 3
    return True


def solve(g1: List[List[int]], g2: List[List[int]]) -> int:
    g3: List[List[int]] = deepcopy(g1)
    for i in range(len(g2)):
        for j in range(len(g2[0])):
            if g1[i][j] != g2[i][j]:
                g3[i][j] = 2
    res: int = 0
    for i in range(len(g3)):
        for j in range(len(g3[0])):
            if g3[i][j] == 1 and _is_new_matching_region(g3, i, j):
                # print(f"_is_new_matching_region(i={i}, j={j})=True\ng3={repr(g3)}")
                res += 1
    return res
