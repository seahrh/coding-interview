"""
Given a binary tree, flatten it into linked list in-place. Usage of auxiliary data structure is not allowed.
After flattening, left of each node should point to NULL and right should contain next node in preorder.
Examples:
Input :
          1
        /   \\
       2     5
      / \     \\
     3   4     6

Output :
    1
     \\
      2
       \\
        3
         \\
          4
           \\
            5
             \\
              6

Input :
        1
       / \\
      3   4
         /
        2
         \\
          5
Output :
     1
      \\
       3
        \\
         4
          \\
           2
            \\
             5

See https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/
"""
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


def solve(root: Node) -> None:
    if root.left is not None:
        solve(root.left)
    if root.right is not None:
        solve(root.right)
    leaf: Optional[Node] = root.left
    while leaf is not None and leaf.right is not None:
        leaf = leaf.right
    right: Optional[Node] = root.right
    if leaf is not None:
        root.right = root.left
        root.left = None
        leaf.right = right
    print(f"root={root}, leaf={leaf}, left={root.left}, right={root.right}")
