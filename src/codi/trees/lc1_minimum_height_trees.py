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
1. Pruning Finds the Tree's Centroids
The roots of Minimum Height Trees (MHTs) must be as close to the centre of the tree as possible;
these are known as the centroids.
The longest path in a tree (called the diameter) will have its midpoint(s) as optimal root choices.
If the diameter’s length is even, there are two centroids.
If it’s odd, there’s one centroid.

2. Pruning Simulation
When you remove the leaves layer-by-layer,
you’re effectively shrinking the tree from the outside towards the center—like peeling an onion.
Each "prune" removes only nodes that can never be in the middle.

3. Why TWO?
A tree's centre will always be one or two nodes:
One node: it's the middle of the path (odd diameter).
Two nodes: it's the two central nodes (even diameter).

Step-by-Step
Build Adjacency List & Degree Array:
For each edge, record the connection in both directions (since the tree is undirected).
Also, keep track of the degree (number of connections) for each node.

Identify Initial Leaves:
Add all nodes with degree 1 (the leaves) to the queue.
These will be the first nodes "pruned" from the tree.

Iterative Pruning Loop:
While there are more than two nodes remaining:
Remove the current batch of leaves.
For each removed leaf, decrease the degree of its neighbors.
If any neighbor becomes a leaf (degree 1), add it to the leaves queue.
When only one or two nodes remain:
Those are the centroids and possible MHT roots, so return them.

Complexity
Time: O(n) — each edge and node processed once.
Space: O(n) — adjacency list and degree array.

References
- Code https://leetcode.com/problems/minimum-height-trees/solutions/827284/c-99-tc-with-explanation-using-bfs-top-sort/
- Explanation https://leetcode.com/problems/minimum-height-trees/solutions/1631179/c-python-3-simple-solution-w-explanation-brute-force-2x-dfs-remove-leaves-w-bfs/
"""

from collections import deque
from typing import Deque, List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Special case: single node tree
        if n == 1:
            return [0]
        adj: List[List[int]] = [[] for _ in range(n)]
        deg: List[int] = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            deg[a] += 1
            deg[b] += 1
        # Start with all leaf nodes (nodes of degree 1)
        leaves: Deque[int] = deque(i for i in range(n) if deg[i] == 1)
        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in adj[leaf]:
                    deg[neighbor] -= 1
                    if deg[neighbor] == 1:
                        leaves.append(neighbor)
        # The remaining nodes are the centroids (roots of MHTs)
        return list(leaves)
