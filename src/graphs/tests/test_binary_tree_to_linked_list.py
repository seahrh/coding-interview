from graphs.binary_tree_to_linked_list import *


class TestBinaryTreeToLinkedList:
    def test_3_nodes_or_less(self):
        n1 = Node(1)
        solve(n1)
        assert n1.left is None and n1.right is None
        n2 = Node(2)
        n1.left = n2
        solve(n1)
        assert n1.left is None and n1.right == n2
        assert n2.left is None and n2.right is None
        n3 = Node(3)
        n1.left = None
        n1.right = n3
        solve(n1)
        assert n1.left is None and n1.right == n3
        assert n3.left is None and n3.right is None
        n1.left = n2
        n1.right = n3
        solve(n1)
        assert n1.left is None and n1.right == n2
        assert n2.left is None and n2.right == n3
        assert n3.left is None and n3.right is None
