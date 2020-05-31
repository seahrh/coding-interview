from graphs.binary_tree import *


class TestBinaryInsert:
    def test_binary_insert(self):
        root = Node(3)
        insert_bst(root, Node(7))
        insert_bst(root, Node(1))
        insert_bst(root, Node(5))
        assert root.data == 3
        assert root.left.data == 1
        assert root.right.data == 7
        assert root.right.left.data == 5


class TestInOrderTraversal:
    def test_in_order_traverse(self):
        root = Node(3)
        insert_bst(root, Node(7))
        insert_bst(root, Node(1))
        insert_bst(root, Node(5))
        path = in_order_traverse(root)
        assert [node.data for node in path] == [1, 3, 5, 7]


class TestPreOrderTraversal:
    def test_pre_order_traverse(self):
        root = Node(3)
        insert_bst(root, Node(7))
        insert_bst(root, Node(1))
        insert_bst(root, Node(5))
        path = pre_order_traverse(root)
        assert [node.data for node in path] == [3, 1, 7, 5]


class TestMaxNode:
    def test_single_node_tree(self):
        root = Node(3)
        assert max_node(root).data == 3

    def test_tree_has_left_subtree_but_empty_right_subtree(self):
        root = Node(3)
        insert_bst(root, Node(1))
        assert max_node(root).data == 3

    def test_tree_has_both_left_and_right_subtrees(self):
        root = Node(3)
        insert_bst(root, Node(7))
        insert_bst(root, Node(1))
        insert_bst(root, Node(5))
        assert max_node(root).data == 7


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


class TestGetInOrder:
    def test_single_node_tree(self):
        root = Node(3)
        assert get_in_order(root, index=1).data == 3
        assert get_in_order(root, index=2) is None

    def test_tree_has_left_subtree_but_empty_right_subtree(self):
        root = Node(3)
        insert_bst(root, Node(1))
        insert_bst(root, Node(2))
        assert get_in_order(root, index=1).data == 1
        assert get_in_order(root, index=2).data == 2
        assert get_in_order(root, index=3).data == 3
        assert get_in_order(root, index=4) is None

    def test_tree_has_both_left_and_right_subtrees(self):
        root = Node(3)
        insert_bst(root, Node(5))
        insert_bst(root, Node(1))
        insert_bst(root, Node(2))
        insert_bst(root, Node(4))
        assert get_in_order(root, index=1).data == 1
        assert get_in_order(root, index=2).data == 2
        assert get_in_order(root, index=3).data == 3
        assert get_in_order(root, index=4).data == 4
        assert get_in_order(root, index=5).data == 5
        assert get_in_order(root, index=6) is None
