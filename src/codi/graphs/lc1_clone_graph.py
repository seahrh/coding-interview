"""
133. Clone Graph https://leetcode.com/problems/clone-graph/description/

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}
Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

SOLUTION
Cloning a graph involves creating new nodes that mirror the values and connections of the original graph,
such that changing the clone won’t affect the original.
The main challenges:
Nodes may be referenced multiple times (by neighbors).
To avoid creating duplicate nodes, we need a way to keep track of which nodes have already been cloned.
The graph may contain cycles.
This is commonly solved using DFS (Depth-First Search) or BFS (Breadth-First Search), tracking clones with a hashmap.
Clone Mapping
Use a dictionary (cloned) to map each original node to its cloned node, preventing duplicates and handling cycles.
Depth-First Search (DFS)
Start from the given node.
If the current node has already been cloned, return it.
Otherwise, create a new clone, store it in the dictionary, and recursively clone all its neighbors.
Neighbor Handling
Recursively add each neighbor's clone to the current node's neighbor list.
"""

from typing import Dict, Optional

from codi.graphs import Node


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        # Dictionary to save cloned nodes
        cloned: Dict[Node, Node] = {}

        def dfs(current):
            if current in cloned:
                return cloned[current]
            # Create a new clone
            copy = Node(current.val)
            cloned[current] = copy
            # Clone all neighbors recursively
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
