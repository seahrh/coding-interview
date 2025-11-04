"""
105. Construct Binary Tree from Preorder and Inorder Traversal https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Given two integer arrays preorder and inorder where
preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
**preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

SOLUTION
Preorder Traversal: Always starts with the root, then explores the left subtree, then the right.
Inorder Traversal: Explores left subtree first, then the root, then the right subtree.

How does this solve the problem?
The first value in `preorder` is the root (preorder[pre_lo]).
Find the root's position in `inorder` (in_root_idx).
All elements left of root in inorder are the left subtree; elements right are the right subtree.
Recursively apply this logic for both subtrees.
Use a hash map (value_to_index) for constant-time lookups from value to its index in inorder.

Why use explicit indices (pre_lo, pre_hi, in_lo, in_hi)?
Avoids repeated list slicing; works directly with array boundaries—a performance win.
Keeps space and time complexity manageable, especially for large input sizes.

Time O(N), where N is the number of nodes, due to no repeated slicing and efficient lookups.
Space O(N) for the hashmap and recursion stack in worst case.

References
- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/3169574/solution/
- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/2279180/python-explained/
"""

from typing import Dict, List, Optional

from codi.trees import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for quick lookup
        value_to_index: Dict[int, int] = {
            value: idx for idx, value in enumerate(inorder)
        }

        # Helper: Recursively build tree from preorder/inorder slices
        def build(pre_lo, pre_hi, in_lo, in_hi):
            if pre_lo > pre_hi or in_lo > in_hi:
                return None
            root_val = preorder[pre_lo]
            root = TreeNode(root_val)
            # Index of root in inorder
            in_root_idx = value_to_index[root_val]
            left_size = in_root_idx - in_lo
            # Build left and right subtrees
            root.left = build(pre_lo + 1, pre_lo + left_size, in_lo, in_root_idx - 1)
            root.right = build(pre_lo + left_size + 1, pre_hi, in_root_idx + 1, in_hi)
            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
