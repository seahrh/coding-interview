from graphs.merge_trees import *


class TestMergeTrees:
    # noinspection PyUnresolvedReferences
    def test_recursion(self):
        assert merge_rec(left=None, right=None) is None
        r = merge_rec(left=Node(1), right=None)
        assert r.data == 1 and r.left is None and r.right is None
        r = merge_rec(left=None, right=Node(2))
        assert r.data == 2 and r.left is None and r.right is None
        r = merge_rec(left=Node(1), right=Node(2))
        assert r.data == 3 and r.left is None and r.right is None
        r = merge_rec(
            left=Node(
                1,
                left=Node(2, left=Node(4), right=Node(5)),
                right=Node(3, left=Node(6), right=Node(7)),
            ),
            right=Node(
                5,
                left=Node(7, left=Node(2), right=Node(4)),
                right=Node(3, left=Node(1), right=Node(6)),
            ),
        )
        assert r.data == 6
        assert r.left.data == 9
        assert r.left.left.data == 6
        assert r.left.right.data == 9
        assert r.right.data == 6
        assert r.right.left.data == 7
        assert r.right.right.data == 13
        r = merge_rec(
            left=Node(1, left=Node(2, right=Node(5)), right=Node(3, right=Node(7)),),
            right=Node(5, left=Node(7, right=Node(4)), right=Node(3, left=Node(1)),),
        )
        assert r.data == 6
        assert r.left.data == 9
        assert r.left.left is None
        assert r.left.right.data == 9
        assert r.right.data == 6
        assert r.right.left.data == 1
        assert r.right.right.data == 7

    # noinspection PyUnresolvedReferences
    def test_iteration(self):
        assert merge(left=None, right=None) is None
        r = merge(left=Node(1), right=None)
        assert r.data == 1 and r.left is None and r.right is None
        r = merge(left=None, right=Node(2))
        assert r.data == 2 and r.left is None and r.right is None
        r = merge(left=Node(1), right=Node(2))
        assert r.data == 3 and r.left is None and r.right is None
        r = merge(
            left=Node(
                1,
                left=Node(2, left=Node(4), right=Node(5)),
                right=Node(3, left=Node(6), right=Node(7)),
            ),
            right=Node(
                5,
                left=Node(7, left=Node(2), right=Node(4)),
                right=Node(3, left=Node(1), right=Node(6)),
            ),
        )
        assert r.data == 6
        assert r.left.data == 9
        assert r.left.left.data == 6
        assert r.left.right.data == 9
        assert r.right.data == 6
        assert r.right.left.data == 7
        assert r.right.right.data == 13
        r = merge(
            left=Node(1, left=Node(2, right=Node(5)), right=Node(3, right=Node(7)),),
            right=Node(5, left=Node(7, right=Node(4)), right=Node(3, left=Node(1)),),
        )
        assert r.data == 6
        assert r.left.data == 9
        assert r.left.left is None
        assert r.left.right.data == 9
        assert r.right.data == 6
        assert r.right.left.data == 1
        assert r.right.right.data == 7
