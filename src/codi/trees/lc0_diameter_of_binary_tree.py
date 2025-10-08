"""
543. Diameter of Binary Tree https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:
Input: root = [1,2]
Output: 1
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100

SOLUTION
A subtree may have a larger diameter than its ancestor, as the ancestor subtree can be skewed/lopsided.
Hence the longest path may not pass through the root.
DFS find the max diameter at every node.
References
- https://leetcode.com/problems/diameter-of-binary-tree/solutions/1515564/python-easy-to-understand-solution-w-explanation/
"""

from typing import Optional

from codi.trees import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0

        def dfs(root: Optional[TreeNode]) -> int:
            """Find the max depth of the subtree."""
            nonlocal mx
            if root is None:
                return 0
            lef = dfs(root.left)
            rig = dfs(root.right)
            mx = max(mx, lef + rig)  # diameter of this subtree
            return 1 + max(lef, rig)

        dfs(root)
        return mx
