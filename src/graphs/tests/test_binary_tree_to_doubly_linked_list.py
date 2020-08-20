from graphs.binary_tree_to_doubly_linked_list import *


class TestBinaryTreeToDoublyLinkedList:
    def test_3_nodes_or_less(self):
        n1 = Node(1)
        solve(n1)
        assert n1.prev is None and n1.next is None
        n2 = Node(2)
        n1.left = n2
        solve(n1)
        assert n1.prev == n2 and n1.next is None
        assert n2.prev is None and n2.next == n1
        n3 = Node(3)
        n1.right = n3
        solve(n1)
        assert n1.prev == n2 and n1.next == n3
        assert n2.prev is None and n2.next == n1
        assert n3.prev == n1 and n3.next is None

    def test_case_1(self):
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n2 = Node(2, left=n4, right=n5)
        n3 = Node(3, left=n6, right=n7)
        n1 = Node(1, left=n2, right=n3)
        solve(n1)
        assert n4.prev is None and n4.next == n2
        assert n2.prev == n4 and n2.next == n5
        assert n5.prev == n2 and n5.next == n1
        assert n1.prev == n5 and n1.next == n6
        assert n6.prev == n1 and n6.next == n3
        assert n3.prev == n6 and n3.next == n7
        assert n7.prev == n3 and n7.next is None

    def test_case_2(self):
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n2 = Node(2, right=n5)
        n3 = Node(3, left=n6, right=n7)
        n1 = Node(1, left=n2, right=n3)
        solve(n1)
        assert n2.prev is None and n2.next == n5
        assert n5.prev == n2 and n5.next == n1
        assert n1.prev == n5 and n1.next == n6
        assert n6.prev == n1 and n6.next == n3
        assert n3.prev == n6 and n3.next == n7
        assert n7.prev == n3 and n7.next is None

    def test_case_3(self):
        n4 = Node(4)
        n6 = Node(6)
        n7 = Node(7)
        n2 = Node(2, left=n4)
        n3 = Node(3, left=n6, right=n7)
        n1 = Node(1, left=n2, right=n3)
        solve(n1)
        assert n4.prev is None and n4.next == n2
        assert n2.prev == n4 and n2.next == n1
        assert n1.prev == n2 and n1.next == n6
        assert n6.prev == n1 and n6.next == n3
        assert n3.prev == n6 and n3.next == n7
        assert n7.prev == n3 and n7.next is None

    def test_case_4(self):
        n4 = Node(4)
        n5 = Node(5)
        n7 = Node(7)
        n2 = Node(2, left=n4, right=n5)
        n3 = Node(3, right=n7)
        n1 = Node(1, left=n2, right=n3)
        solve(n1)
        assert n4.prev is None and n4.next == n2
        assert n2.prev == n4 and n2.next == n5
        assert n5.prev == n2 and n5.next == n1
        assert n1.prev == n5 and n1.next == n3
        assert n3.prev == n1 and n3.next == n7
        assert n7.prev == n3 and n7.next is None

    def test_case_5(self):
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n2 = Node(2, left=n4, right=n5)
        n3 = Node(3, left=n6)
        n1 = Node(1, left=n2, right=n3)
        solve(n1)
        assert n4.prev is None and n4.next == n2
        assert n2.prev == n4 and n2.next == n5
        assert n5.prev == n2 and n5.next == n1
        assert n1.prev == n5 and n1.next == n6
        assert n6.prev == n1 and n6.next == n3
        assert n3.prev == n6 and n3.next is None
