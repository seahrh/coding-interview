from recursion.binode import *


class TestBinode:
    @staticmethod
    def assert_doubly_linked_list(head, expected_list):
        a = []
        node = head
        while node is not None:
            a.append(node.key)
            node = node.right
        assert a == expected_list
        while node is not None:
            assert a.pop() == node.key
            node = node.left

    def test_given_empty_tree_then_return_none(self):
        assert BiNode.as_linked_list(None) is None

    def test_given_tree_of_size_one_then_return_root(self):
        head = BiNode.as_linked_list(BiNode(key=20, left=None, right=None))
        self.assert_doubly_linked_list(head, [20])

    def test_given_empty_right_subtree(self):
        head = BiNode.as_linked_list(
            BiNode(key=20,
                   left=BiNode(key=10, left=None, right=None),
                   right=None))
        self.assert_doubly_linked_list(head, [10, 20])

    def test_given_empty_left_subtree(self):
        head = BiNode.as_linked_list(
            BiNode(key=20,
                   left=None,
                   right=BiNode(key=30, left=None, right=None)))
        self.assert_doubly_linked_list(head, [20, 30])

    def test_given_example(self):
        head = BiNode.as_linked_list(
            BiNode(key=40,
                   left=BiNode(key=20, left=BiNode(key=10, left=BiNode(key=0)), right=BiNode(key=30)),
                   right=BiNode(key=50, right=BiNode(key=60))))
        self.assert_doubly_linked_list(head, [0, 10, 20, 30, 40, 50, 60])
