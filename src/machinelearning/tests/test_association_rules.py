from machinelearning.association_rules import *


class TestBinaryPartition:
    def test_binary_partition(self):
        assert binary_partition({"a", "b"}) == {
            Partitions(left=frozenset({"a"}), right=frozenset({"b"})),
            Partitions(left=frozenset({"b"}), right=frozenset({"a"})),
        }
        assert binary_partition({"a", "b", "c"}) == {
            Partitions(left=frozenset({"a"}), right=frozenset({"b", "c"})),
            Partitions(left=frozenset({"b"}), right=frozenset({"a", "c"})),
            Partitions(left=frozenset({"c"}), right=frozenset({"a", "b"})),
            Partitions(left=frozenset({"b", "c"}), right=frozenset({"a"})),
            Partitions(left=frozenset({"c", "a"}), right=frozenset({"b"})),
            Partitions(left=frozenset({"b", "a"}), right=frozenset({"c"})),
        }
        assert binary_partition({"a", "b", "c", "d"}) == {
            Partitions(left=frozenset({"a"}), right=frozenset({"b", "c", "d"})),
            Partitions(left=frozenset({"b"}), right=frozenset({"a", "c", "d"})),
            Partitions(left=frozenset({"c"}), right=frozenset({"a", "b", "d"})),
            Partitions(left=frozenset({"d"}), right=frozenset({"a", "b", "c"})),
            Partitions(left=frozenset({"a", "b"}), right=frozenset({"d", "c"})),
            Partitions(left=frozenset({"d", "b"}), right=frozenset({"a", "c"})),
            Partitions(left=frozenset({"d", "a"}), right=frozenset({"c", "b"})),
            Partitions(left=frozenset({"a", "c"}), right=frozenset({"d", "b"})),
            Partitions(left=frozenset({"c", "b"}), right=frozenset({"d", "a"})),
            Partitions(left=frozenset({"d", "c"}), right=frozenset({"a", "b"})),
            Partitions(
                left=frozenset({"d", "a", "b"}), right=frozenset({"c"})
            ),  # LHS drop 'c'
            Partitions(
                left=frozenset({"a", "c", "b"}), right=frozenset({"d"})
            ),  # LHS drop 'd'
            Partitions(
                left=frozenset({"d", "a", "c"}), right=frozenset({"b"})
            ),  # LHS drop 'b'
            Partitions(
                left=frozenset({"d", "c", "b"}), right=frozenset({"a"})
            ),  # LHS drop 'a'
        }
