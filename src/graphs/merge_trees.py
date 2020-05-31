"""
Given two binary trees, merge them into a new binary tree.
Each tree node contains an integer value.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the non-null node will be used as the node of new tree.

SOLUTION

Recursion approach
- Merging follows pre-order traversal.
- N is the total number of nodes in left and right trees.
- Time O(N)
- Space O(N): recursive call stack

"""
from copy import deepcopy
from typing import Optional
from graphs.binary_tree import Node


def merge_rec(left: Optional[Node[int]], right: Optional[Node[int]]) -> Optional[Node]:
    """Merges the two binary trees and returns the root of the new binary tree."""
    if left is None:
        return deepcopy(right)
    if right is None:
        return deepcopy(left)
    root = Node(data=left.data + right.data)
    root.left = merge_rec(left.left, right.left)
    root.right = merge_rec(left.right, right.right)
    return root
