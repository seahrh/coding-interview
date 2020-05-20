class LinkedListNode:
    def __init__(self, data, prev_node=None, next_node=None):
        self.prev = prev_node
        self.next = next_node
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def remove(self, node):
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
