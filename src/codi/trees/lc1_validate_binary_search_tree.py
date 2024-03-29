"""
98. Validate Binary Search Tree https://leetcode.com/problems/validate-binary-search-tree/description/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
Input: root = [2,1,3]
Output: true
Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

SOLUTION
References
- https://leetcode.com/problems/validate-binary-search-tree/solutions/3169560/solution/
"""
import sys
from typing import Optional

from codi.trees import TreeNode


class Solution:
    def rec(self, root: Optional[TreeNode], vmin: int, vmax: int) -> bool:
        if root is None:
            return True
        if not vmin < root.val < vmax:
            return False
        return self.rec(root.left, vmin=vmin, vmax=root.val) and self.rec(
            root.right, vmin=root.val, vmax=vmax
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root, vmin=-sys.maxsize, vmax=sys.maxsize)
