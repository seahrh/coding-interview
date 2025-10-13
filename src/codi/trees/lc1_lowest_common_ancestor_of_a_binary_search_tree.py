"""
235. Lowest Common Ancestor of a Binary Search Tree https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
Constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the BST.

SOLUTION
The algorithm is a recursive search down a BST.
At each step, you move left or right depending on the relative values of p, q, and root.
In the best case (balanced BST), the search goes down one branch—this takes O(h) time, where h is the tree height.
For a balanced BST with n nodes, h = O(log n).
In the worst case (highly skewed BST, e.g., a linked list), h = O(n).
Time average O(lg N), worst O(N)
Space average O(lg N), worst O(N), recursion stack depth
References
- https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/1347857/c-java-python-iterate-in-bst-picture-explain-time-o-h-space-o-1/
"""

from codi.trees import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Ensure p<q
        if p.val > q.val:
            p, q = q, p

        def rec(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
            if root is None:
                return None
            if p.val <= root.val <= q.val:
                return root
            if p.val > root.val:
                return rec(root.right, p, q)
            return rec(root.left, p, q)

        return rec(root, p, q)
