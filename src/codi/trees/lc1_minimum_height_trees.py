"""
310. Minimum Height Trees https://leetcode.com/problems/minimum-height-trees/description/

A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree,
you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Constraints:
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.

SOLUTION
The MHTs exist in the middle of the longest path (tree diameter).
If longest path is even-length, then there are 2 MHTs else 1 MHT.
BFS iteratively remove leaf nodes until MHTs are left.
Time O(V+E)
Space O(V+E)
References
- Code https://leetcode.com/problems/minimum-height-trees/solutions/827284/c-99-tc-with-explanation-using-bfs-top-sort/
- Explanation https://leetcode.com/problems/minimum-height-trees/solutions/1631179/c-python-3-simple-solution-w-explanation-brute-force-2x-dfs-remove-leaves-w-bfs/
"""

from collections import deque
from typing import Deque, List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        res: List[int] = []
        adj: List[List[int]] = [[] for _ in range(n)]
        deg: List[int] = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            deg[a] += 1
            deg[b] += 1
        q: Deque[int] = deque()
        for i in range(n):
            if deg[i] == 1:
                q.append(i)
        while len(q) != 0:
            res = []
            m = len(q)
            for _ in range(m):
                i = q.popleft()
                res.append(i)
                for j in adj[i]:
                    deg[j] -= 1
                    if deg[j] == 1:
                        q.append(j)
        return res
