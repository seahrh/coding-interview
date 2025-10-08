"""
Flatten a binary tree to a doubly linked list
                1
        2                3
    4        5        6        7

return 4 <-> 2 <-> 5 <-> 1 <-> 6 <-> 3 <-> 7
The "right-most" node in the left subtree is previous to root.
The "left-most" node in the right subtree is next to root.
Update the `previous` and `next` pointers of each node.

SOLUTION
Pass root as the next node to the left subtree, previous node to the right subtree.
Time O(N)
Space O(N): depth of recursive call stack
"""

from typing import Optional


class Node:
    def __init__(
        self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None
    ):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


def _solve(
    root: Node, prev_node: Optional[Node] = None, next_node: Optional[Node] = None
) -> None:
    if root.left is None:
        # right subtree does not have a left child
        # ancestor is previous to root of right subtree
        if prev_node is not None:
            root.prev = prev_node
            prev_node.next = root
    else:
        _solve(root.left, prev_node=prev_node, next_node=root)
    if root.right is None:
        # left subtree does not have a right child
        # ancestor is next to root of left subtree
        if next_node is not None:
            root.next = next_node
            next_node.prev = root
    else:
        _solve(root.right, prev_node=root, next_node=next_node)


def solve(root: Node) -> None:
    _solve(root)
