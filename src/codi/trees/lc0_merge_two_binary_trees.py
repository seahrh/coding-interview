"""
617. Merge Two Binary Trees https://leetcode.com/problems/merge-two-binary-trees/description/

You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees.
Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
Constraints:
The number of nodes in both trees is in the range [0, 2000].
-10^4 <= Node.val <= 10^4

SOLUTION
Recursion approach
- Merging follows pre-order traversal. N is the total number of nodes in left and right trees.
- Time O(N)
- Space O(N): recursive call stack

Iteration approach
- Replace recursion with a stack; each entry is a 2-Tuple of (left tree node, right tree node).
- In the loop, update only the parent and children nodes (ignore grandparents and grandchildren).
- Time O(N)
- Space O(N)

Based on https://leetcode.com/articles/merge-two-binary-trees/
"""

from copy import deepcopy
from typing import List, Optional, Tuple

from codi.trees import TreeNode


class Solution:
    def mergeTreesRec(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """Recursion method"""
        if root1 is None and root2 is None:
            return None
        if root2 is None:
            return root1
        if root1 is None:
            return root2
        res = TreeNode(
            val=root1.val + root2.val,
            left=self.mergeTrees(root1.left, root2.left),
            right=self.mergeTrees(root1.right, root2.right),
        )
        return res

    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """Iterative method"""
        left, right = root1, root2
        if left is None:
            return right
        # root of the new binary tree; clone the left tree before modifying it.
        root: Optional[TreeNode] = deepcopy(left)
        st: List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [(root, right)]
        # in each iteration, update the only parent and children nodes.
        while len(st) != 0:
            left, right = st.pop()
            if (
                left is None or right is None
            ):  # parent node is null, so nothing to merge
                continue
            left.val += right.val
            if left.left is None:
                left.left = right.left
            else:
                st.append((left.left, right.left))
            if left.right is None:
                left.right = right.right
            else:
                st.append((left.right, right.right))
        return root
