from typing import TypeVar, Generic, Optional

T = TypeVar("T")  # Declare type variable


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


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


def in_order_print(root: Optional[Node]) -> None:
    if root is None:
        return
    in_order_print(root.left)
    print(root.data)
    in_order_print(root.right)


def pre_order_print(root: Optional[Node]) -> None:
    if root is None:
        return
    print(root.data)
    pre_order_print(root.left)
    pre_order_print(root.right)
