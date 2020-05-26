from typing import TypeVar, Generic, Optional, List

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


def in_order_traverse(root: Optional[Node]) -> List[Node]:
    res: List[Node] = []
    if root is None:
        return res
    res = res + in_order_traverse(root.left)
    res.append(root)
    res = res + in_order_traverse(root.right)
    return res


def pre_order_print(root: Optional[Node]) -> None:
    if root is None:
        return
    print(root.data)
    pre_order_print(root.left)
    pre_order_print(root.right)
