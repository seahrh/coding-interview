"""
199. Binary Tree Right Side View https://leetcode.com/problems/binary-tree-right-side-view/description/

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:
Input: root = [1,null,3]
Output: [1,3]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        if root is None:
            return res
        q: Deque = deque()  # bfs for level order traversal
        q.append(root)
        while len(q) != 0:
            lv = []
            n = len(q)  # at this point, all nodes in queue belong to same level
            for _ in range(n):
                c = q.popleft()
                if c.left is not None:
                    q.append(c.left)
                if c.right is not None:
                    q.append(c.right)
                lv.append(c.val)
            res.append(lv)
        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return [lv[-1] for lv in self.levelOrder(root)]
