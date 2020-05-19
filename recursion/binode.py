"""
BiNode: Consider a simple data structure called BiNode, which has pointers to two other nodes. The
data structure BiNode could be used to represent both a binary tree (where nodel is the left node
and node2 is the right node) or a doubly linked list (where nodel is the previous node and node2
is the next node). Implement a method to convert a binary search tree (implemented with BiNode)
into a doubly linked list. The values should be kept in order and the operation should be performed
in place (that is, on the original data structure).

(17.12, p571)
SOLUTION: recursion
Left and right halves of the tree form their own "sub-parts" of the linked list (i.e., they
appear consecutively in the linked list). So, if we recursively converted the left and right
subtrees to a doubly linked list, we can build the final linked list from those parts.

How to return the head and tail of a linked list? Return the head of a doubly linked list.

Tree as doubly linked list: form the triangle where root is middle of the list.
      mid
    //   \\
head      tail

If left subtree is not empty, left.next = root, root.prev = left
If right subtree is not empty, root.next = right, right.prev = root
If both left and right subtrees are not empty, right.next = left, left.prev = right

O(n) time: each node is touched an average of O(1) times.
O(n) space: depth of call stack
"""


class BiNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def append(self, other):
        self.right = other
        other.left = self

    @staticmethod
    def as_circular_linked_list(root):
        if root is None:
            return None
        lsub = BiNode.as_circular_linked_list(root.left)
        rsub = BiNode.as_circular_linked_list(root.right)
        if lsub is None and rsub is None:
            root.left = root
            root.right = root
            return root
        rsub_tail = None if rsub is None else rsub.left
        # join left to root
        if lsub is None:
            rsub.left.append(root)
        else:
            lsub.left.append(root)
        # join right to root
        if rsub is None:
            root.append(lsub)
        else:
            root.append(rsub)
        # join right to left
        if lsub is not None and rsub is not None:
            rsub_tail.append(lsub)
        return root if lsub is None else lsub

    @staticmethod
    def as_linked_list(root):
        """Takes the circular linked list and break the circular connection."""
        head = BiNode.as_circular_linked_list(root)
        if head is None:
            return None
        head.left.right = None
        head.left = None
        return head
