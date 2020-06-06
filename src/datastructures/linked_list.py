from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class DLinkedList:
    """Custom implementation of doubly linked list for LRU cache problem to remove node in O(1) time.
    Because python collections.deque remove operation takes O(n) time (removing first instance of value).
    """

    class Node(Generic[T]):
        def __init__(
            self,
            data: T,
            prev_node: Optional["DLinkedList.Node"] = None,
            next_node: Optional["DLinkedList.Node"] = None,
        ):
            self.prev = prev_node
            self.next = next_node
            self.data = data

    def __init__(self):
        self.head: Optional[DLinkedList.Node] = None
        self.tail: Optional[DLinkedList.Node] = None
        self.len = 0

    def __len__(self):
        return self.len

    def remove(self, node):
        """Remove node in O(1) time."""
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        self.len -= 1

    def append_left(self, node):
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
        self.head = node
        self.len += 1

    def pop(self):
        res = self.tail
        self.remove(res)
        return res
