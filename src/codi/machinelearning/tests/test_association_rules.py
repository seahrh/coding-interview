from codi.machinelearning.association_rules import *


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


class TestFrequentItemsets:
    def test_when_input_is_empty_then_return_empty_output(self):
        assert frequent_itemsets([], minsup=0.5, k=1) == [[]]

    def test_3_itemsets(self):
        assert frequent_itemsets(
            [
                Pair(basket_id=1, item_id=2),
                Pair(basket_id=1, item_id=3),
                Pair(basket_id=1, item_id=4),
                Pair(basket_id=1, item_id=5),
                Pair(basket_id=2, item_id=1),
                Pair(basket_id=2, item_id=2),
                Pair(basket_id=2, item_id=4),
                Pair(basket_id=2, item_id=5),
                Pair(basket_id=3, item_id=1),
                Pair(basket_id=3, item_id=2),
                Pair(basket_id=3, item_id=4),
                Pair(basket_id=3, item_id=5),
                Pair(basket_id=3, item_id=6),
                Pair(basket_id=4, item_id=1),
                Pair(basket_id=4, item_id=2),
                Pair(basket_id=4, item_id=3),
                Pair(basket_id=4, item_id=4),
                Pair(basket_id=4, item_id=5),
                Pair(basket_id=5, item_id=5),
                Pair(basket_id=5, item_id=1),
                Pair(basket_id=6, item_id=5),
                Pair(basket_id=6, item_id=2),
                Pair(basket_id=7, item_id=5),
                Pair(basket_id=7, item_id=4),
                Pair(basket_id=8, item_id=4),
            ],
            minsup=0.5,
            k=3,
        ) == [
            [
                Itemset(support_count=7, items={5}),
                Itemset(support_count=6, items={4}),
                Itemset(support_count=5, items={2}),
                Itemset(support_count=4, items={1}),
            ],
            [
                Itemset(support_count=5, items={2, 5}),
                Itemset(support_count=5, items={4, 5}),
                Itemset(support_count=4, items={1, 5}),
                Itemset(support_count=4, items={2, 4}),
            ],
            [Itemset(support_count=4, items={2, 4, 5})],
        ]


class TestRules:
    def test_when_input_is_empty_then_return_empty_output(self):
        assert rules([], minsup=0.5, k=1, minconf=0.5) == []

    def test_3_itemsets(self):
        assert rules(
            [
                Pair(basket_id=1, item_id=2),
                Pair(basket_id=1, item_id=3),
                Pair(basket_id=1, item_id=4),
                Pair(basket_id=1, item_id=5),
                Pair(basket_id=2, item_id=1),
                Pair(basket_id=2, item_id=2),
                Pair(basket_id=2, item_id=4),
                Pair(basket_id=2, item_id=5),
                Pair(basket_id=3, item_id=1),
                Pair(basket_id=3, item_id=2),
                Pair(basket_id=3, item_id=4),
                Pair(basket_id=3, item_id=5),
                Pair(basket_id=3, item_id=6),
                Pair(basket_id=4, item_id=1),
                Pair(basket_id=4, item_id=2),
                Pair(basket_id=4, item_id=3),
                Pair(basket_id=4, item_id=4),
                Pair(basket_id=4, item_id=5),
                Pair(basket_id=5, item_id=5),
                Pair(basket_id=5, item_id=1),
                Pair(basket_id=6, item_id=5),
                Pair(basket_id=6, item_id=2),
                Pair(basket_id=7, item_id=5),
                Pair(basket_id=7, item_id=4),
                Pair(basket_id=8, item_id=4),
            ],
            minsup=0.5,
            k=3,
            minconf=0.001,
        ) == [
            Rule(
                confidence=1.0,
                support=0.625,
                antecedent=frozenset({2}),
                consequent=frozenset({5}),
            ),
            Rule(
                confidence=1.0,
                support=0.5,
                antecedent=frozenset({1}),
                consequent=frozenset({5}),
            ),
            Rule(
                confidence=1.0,
                support=0.5,
                antecedent=frozenset({2, 4}),
                consequent=frozenset({5}),
            ),
            Rule(
                confidence=0.8333333333333334,
                support=0.625,
                antecedent=frozenset({4}),
                consequent=frozenset({5}),
            ),
            Rule(
                confidence=0.8,
                support=0.5,
                antecedent=frozenset({4, 5}),
                consequent=frozenset({2}),
            ),
            Rule(
                confidence=0.8,
                support=0.5,
                antecedent=frozenset({2, 5}),
                consequent=frozenset({4}),
            ),
            Rule(
                confidence=0.8,
                support=0.5,
                antecedent=frozenset({2}),
                consequent=frozenset({4, 5}),
            ),
            Rule(
                confidence=0.8,
                support=0.5,
                antecedent=frozenset({2}),
                consequent=frozenset({4}),
            ),
            Rule(
                confidence=0.7142857142857143,
                support=0.625,
                antecedent=frozenset({5}),
                consequent=frozenset({2}),
            ),
            Rule(
                confidence=0.7142857142857143,
                support=0.625,
                antecedent=frozenset({5}),
                consequent=frozenset({4}),
            ),
            Rule(
                confidence=0.6666666666666666,
                support=0.5,
                antecedent=frozenset({4}),
                consequent=frozenset({2, 5}),
            ),
            Rule(
                confidence=0.6666666666666666,
                support=0.5,
                antecedent=frozenset({4}),
                consequent=frozenset({2}),
            ),
            Rule(
                confidence=0.5714285714285714,
                support=0.5,
                antecedent=frozenset({5}),
                consequent=frozenset({1}),
            ),
            Rule(
                confidence=0.5714285714285714,
                support=0.5,
                antecedent=frozenset({5}),
                consequent=frozenset({2, 4}),
            ),
        ]
