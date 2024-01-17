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
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

SOLUTION
Inorder traversal: LEFT, ROOT, RIGHT
Preorder traversal: ROOT, LEFT, RIGHT
The first element in preorder is the root of the tree. Let it be x
Elements left to x in inorder make up the LEFT subtree.
Elements right to x in inorder make up the RIGHT subtree.
References
- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/3169574/solution/
- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/2279180/python-explained/
"""
from typing import Dict, List, Optional

from codi.trees import TreeNode


class Solution:
    def rec(
        self,
        preorder: List[int],
        inorder: List[int],
        plo: int,
        phi: int,
        ilo: int,
        ihi: int,
        v2i: Dict[int, int],
    ) -> Optional[TreeNode]:
        if plo > phi or ilo > ihi:  # base case: subarray is empty
            return None
        root = TreeNode(preorder[plo])
        i = v2i[preorder[plo]]
        n = i - ilo  # num elements in left subtree
        root.left = self.rec(
            preorder, inorder, plo=plo + 1, phi=plo + n, ilo=ilo, ihi=i - 1, v2i=v2i
        )
        root.right = self.rec(
            preorder, inorder, plo=plo + 1 + n, phi=phi, ilo=i + 1, ihi=ihi, v2i=v2i
        )
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        v2i: Dict[int, int] = {k: v for v, k in enumerate(inorder)}
        plo, phi = 0, len(preorder) - 1
        ilo, ihi = 0, len(inorder) - 1
        return self.rec(preorder, inorder, plo=plo, phi=phi, ilo=ilo, ihi=ihi, v2i=v2i)
