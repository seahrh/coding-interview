from graphs.binary_search_tree import *


class TestBinaryInsert:
    def test_binary_insert(self):
        root = Node(3)
        binary_insert(root, Node(7))
        binary_insert(root, Node(1))
        binary_insert(root, Node(5))
        assert root.data == 3
        assert root.left.data == 1
        assert root.right.data == 7
        assert root.right.left.data == 5


class TestInOrderTraversal:
    def test_in_order_traverse(self):
        root = Node(3)
        binary_insert(root, Node(7))
        binary_insert(root, Node(1))
        binary_insert(root, Node(5))
        path = in_order_traverse(root)
        assert [node.data for node in path] == [1, 3, 5, 7]


class TestPreOrderTraversal:
    def test_pre_order_traverse(self):
        root = Node(3)
        binary_insert(root, Node(7))
        binary_insert(root, Node(1))
        binary_insert(root, Node(5))
        path = pre_order_traverse(root)
        assert [node.data for node in path] == [3, 1, 7, 5]


class TestIsBinarySearchTree:
    def test_is_binary_search_tree(self):
        root = Node(1)
        assert is_binary_search_tree(root)
        root = Node(5, left=Node(3), right=Node(7))
        assert is_binary_search_tree(root)
        root = Node(
            5,
            left=Node(3, left=Node(1), right=Node(4)),
            right=Node(7, left=Node(6), right=Node(9)),
        )
        assert is_binary_search_tree(root)
        root = Node(
            5,
            left=Node(3, left=Node(1), right=Node(40)),
            right=Node(7, left=Node(6), right=Node(9)),
        )
        assert not is_binary_search_tree(root)
        root = Node(
            5,
            left=Node(3, left=Node(1), right=Node(4)),
            right=Node(10, left=Node(6), right=Node(9)),
        )
        assert is_binary_search_tree(root)
