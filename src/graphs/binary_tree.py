from collections import deque
from typing import TypeVar, Generic, Optional, List, Deque


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
        self, data: T, left: Optional["Node"] = None, right: Optional["Node"] = None
    ):
        self.data: T = data
        self.left: Optional["Node"] = left
        self.right: Optional["Node"] = right


def insert_bst(root: Node, node: Node) -> None:
    """Add a node to a binary search tree."""
    if root is None:
        raise ValueError("Tree must have a root")
    if root.data > node.data:
        if root.left is None:
            root.left = node
        else:
            insert_bst(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert_bst(root.right, node)


def in_order_traverse(root: Optional[Node]) -> List[Node]:
    res: List[Node] = []
    if root is None:
        return res
    res += in_order_traverse(root.left)
    res.append(root)
    res += in_order_traverse(root.right)
    return res


def pre_order_traverse(root: Optional[Node]) -> List[Node]:
    res: List[Node] = []
    if root is None:
        return res
    res.append(root)
    res += pre_order_traverse(root.left)
    res += pre_order_traverse(root.right)
    return res


def max_node_bst(root: Optional[Node]) -> Optional[Node]:
    """Returns the last node of the in-order traversal path in the binary search tree."""
    if root is None:
        return None
    if root.right is not None:
        return max_node_bst(root.right)
    # ignore the left subtree
    return root


def max_node(root: Optional[Node]) -> Optional[Node]:
    """Returns the max node of a binary tree."""
    if root is None:
        return None
    res: Node = root
    q: Deque[Node] = deque()
    if root.left is not None:
        q.append(root.left)
    if root.right is not None:
        q.append(root.right)
    while len(q) != 0:
        curr = q.popleft()
        if curr.data > res.data:
            res = curr
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
    return res


def is_binary_search_tree(root: Node) -> bool:
    """
    N is the number of nodes in the binary tree.
    Time O(N): same as in-order traversal
    Space O(1): do not need to store path (unlike in-order traversal)

    :param root: root of the input tree
    :return: True if the tree is BST
    """
    if root is None:
        raise ValueError("Tree must have a root")
    left = max_node(root.left)
    if left is not None and root.data < left.data:
        return False
    right = max_node(root.right)
    if right is not None and root.data > right.data:
        return False
    return True


def get_in_order(root: Node, index: int) -> Optional[Node]:
    """Do in-order traversal of binary tree and return the ith node.
    Because of index, traversal must be done iteratively instead of recursion.
    Return None if index exceeds tree length.
    Time O(N)
    Space O(lg N)
    - Size of stack
    - Better than recursion O(N) because aux array not required to hold full path
    """
    if root is None:
        raise ValueError("Tree must have a root")
    if index < 1:
        raise ValueError("Index starts from 1")
    st: Deque[Node] = deque()
    curr: Optional[Node] = root
    length = 0
    while len(st) != 0 or curr is not None:
        if curr is not None:
            st.append(curr)
            curr = curr.left
            continue
        # traversed all nodes to the left
        curr = st.pop()
        length += 1
        if length == index:
            break
        curr = curr.right
    return curr
