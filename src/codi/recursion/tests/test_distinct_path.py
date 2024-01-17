from codi.recursion.distinct_path import *


class TestDistinctPath:
    def test_longest_path(self):
        assert longest_path(Node(1)) == 1
        assert (
            longest_path(
                Node(
                    1,
                    left=Node(2, left=Node(1), right=Node(2)),
                    right=Node(2, left=Node(4), right=Node(1)),
                )
            )
            == 3
        )
        assert (
            longest_path(
                Node(
                    1,
                    left=Node(2, left=Node(4), right=Node(5)),
                    right=Node(
                        3, left=Node(6, right=Node(8)), right=Node(3, right=Node(9))
                    ),
                )
            )
            == 4
        )
        assert (
            longest_path(
                Node(
                    1,
                    left=Node(2, left=Node(3, left=Node(2)), right=Node(6)),
                    right=Node(
                        3, left=Node(3), right=Node(1, left=Node(5), right=Node(6))
                    ),
                )
            )
            == 3
        )
        assert (
            longest_path(
                Node(1, right=Node(2, left=Node(1), right=Node(1, left=Node(4))))
            )
            == 2
        )
