"""
110. Balanced Binary Tree https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced:
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:
Input: root = []
Output: true
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4

SOLUTION
References
- https://leetcode.com/problems/balanced-binary-tree/solutions/2428871/very-easy-100-fully-explained-c-java-python-javascript-python3/
"""

from typing import Optional

from codi.trees import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            lef, rig = height(root.left), height(root.right)
            # check whether subtree is balanced!
            if lef < 0 or rig < 0 or abs(lef - rig) > 1:
                return -1
            return 1 + max(lef, rig)

        return height(root) >= 0
