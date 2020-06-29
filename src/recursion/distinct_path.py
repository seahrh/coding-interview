r"""
Root to leaf path with maximum distinct nodes
Given a Binary Tree, find count of distinct nodes in a root to leaf path with maximum distinct nodes.
A distinct path is a sequence of nodes that starts at the root, follows the tree edges and contains only
distinct values. Find the number of nodes on the longest distinct path.

EXAMPLE
Input :   1
        /    \
       2      3
      / \    /  \
     4   5  6    3
             \   \
              8   9
Output : 4
The longest distinct path is nodes is 1-3-6-8.

See https://www.geeksforgeeks.org/root-leaf-path-maximum-distinct-nodes/

SOLUTION
N is the number of nodes in the tree.
Time O(N)
Space O(N^2): unbalanced tree in the worst case, depth of recursive call stack.
Balanced tree takes O((lg N)^2) space; create lg N `seen` sets and size of each set is lg N.

"""
from typing import NamedTuple, Set, Optional


class Node(NamedTuple):
    x: int
    left: Optional["Node"] = None  # type: ignore
    right: Optional["Node"] = None  # type: ignore


def _longest_path(root: Optional[Node], seen: Set[int]) -> int:
    if root is None:
        return len(seen)
    if root.x in seen:
        return len(seen)
    seen.add(root.x)
    return max(
        _longest_path(root.left, seen=set(seen)),
        _longest_path(root.right, seen=set(seen)),
    )


def longest_path(root: Node) -> int:
    """Returns length of longest distinct path that starts from the root."""
    seen: Set[int] = set()
    return _longest_path(root, seen)
