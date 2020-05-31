"""
Given two binary trees, merge them into a new binary tree.
Each tree node contains an integer value.
Merge rules:
- Merging starts from the root nodes of both trees.
- If two nodes overlap, then sum node values up as the new value of the merged node.
- Otherwise, the non-null node will be used as the node of new tree.

SOLUTION

Recursion approach
- Merging follows pre-order traversal.
- N is the total number of nodes in left and right trees.
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
from typing import Optional, List, Tuple
from graphs.binary_tree import Node


def merge_rec(
    left: Optional[Node[int]], right: Optional[Node[int]]
) -> Optional[Node[int]]:
    """Merges the two binary trees and returns the root of the new binary tree."""
    if left is None:
        return deepcopy(right)
    if right is None:
        return deepcopy(left)
    root = Node(data=left.data + right.data)
    root.left = merge_rec(left.left, right.left)
    root.right = merge_rec(left.right, right.right)
    return root


def merge(left: Optional[Node[int]], right: Optional[Node[int]]) -> Optional[Node[int]]:
    """Merges the two binary trees and returns the root of the new binary tree."""
    if left is None:
        return deepcopy(right)
    # root of the new binary tree; clone the left tree before modifying it.
    root: Optional[Node] = deepcopy(left)
    st: List[Tuple[Optional[Node[int]], Optional[Node[int]]]] = [(root, right)]
    # in each iteration, update the only parent and children nodes.
    while len(st) != 0:
        l_node, r_node = st.pop()
        if l_node is None or r_node is None:  # parent node is null, so nothing to merge
            continue
        l_node.data += r_node.data
        if l_node.left is None:
            l_node.left = r_node.left
        else:
            st.append((l_node.left, r_node.left))
        if l_node.right is None:
            l_node.right = r_node.right
        else:
            st.append((l_node.right, r_node.right))
    return root
