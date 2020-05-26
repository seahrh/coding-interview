from graphs.binary_search_tree import *


class TestBinarySearchTree:
    def test_binary_insert(self):
        root = Node(3)
        binary_insert(root, Node(7))
        binary_insert(root, Node(1))
        binary_insert(root, Node(5))
        assert root.data == 3
        assert root.left.data == 1
        assert root.right.data == 7
        assert root.right.left.data == 5
