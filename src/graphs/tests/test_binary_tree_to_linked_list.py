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

    def test_case_1(self):
        n3 = Node(3)
        n4 = Node(4)
        n6 = Node(6)
        n2 = Node(2, left=n3, right=n4)
        n5 = Node(5, right=n6)
        n1 = Node(1, left=n2, right=n5)
        solve(n1)
        assert n1.left is None and n1.right == n2
        assert n2.left is None and n2.right == n3
        assert n3.left is None and n3.right == n4
        assert n4.left is None and n4.right == n5
        assert n5.left is None and n5.right == n6
        assert n6.left is None and n6.right is None

    def test_case_2(self):
        n5 = Node(5)
        n2 = Node(2, right=n5)
        n4 = Node(4, left=n2)
        n3 = Node(3)
        n1 = Node(1, left=n3, right=n4)
        solve(n1)
        assert n1.left is None and n1.right == n3
        assert n3.left is None and n3.right == n4
        assert n4.left is None and n4.right == n2
        assert n2.left is None and n2.right == n5
        assert n5.left is None and n5.right is None
