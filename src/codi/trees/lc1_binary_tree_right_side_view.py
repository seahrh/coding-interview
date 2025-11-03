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

SOLUTION
Level order (or breadth-first search) is a different approach
that visits nodes level by level from left to right, using a queue instead of recursion.
"""

from collections import deque
from typing import List, Optional

from codi.trees import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        view: List[int] = []
        queue = deque([root])
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                # Enqueue left and right children (for next level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # If it's the last node in this level, add to the view
                if i == level_length - 1:
                    view.append(node.val)
        return view
