from typing import TypeVar, Generic, Optional, List

T = TypeVar("T")  # Declare type variable


class Node(Generic[T]):
    def __init__(
        self, data: T, left: Optional["Node"] = None, right: Optional["Node"] = None
    ):
        self.data: T = data
        self.left: Optional["Node"] = left
        self.right: Optional["Node"] = right


def binary_insert(root: Node, node: Node) -> None:
    if root is None:
        raise ValueError("Tree must have a root")
    if root.data > node.data:
        if root.left is None:
            root.left = node
        else:
            binary_insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            binary_insert(root.right, node)


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


def max_node(root: Optional[Node]) -> Optional[Node]:
    """Returns the last node of the in-order traversal path in the rooted tree."""
    if root is None:
        return None
    if root.right is not None:
        return max_node(root.right)
    # ignore the left subtree
    return root


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
