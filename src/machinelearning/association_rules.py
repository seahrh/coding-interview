from collections import defaultdict
from itertools import combinations
from typing import (
    NamedTuple,
    Set,
    Iterable,
    Tuple,
    FrozenSet,
    Hashable,
    List,
    DefaultDict,
)


class Itemset(NamedTuple):
    support_count: int
    items: Set[Hashable]


class Rule(NamedTuple):
    confidence: float
    support: float
    antecedent: Itemset
    consequent: Itemset


def _key(items: Iterable[Hashable]) -> Tuple[Hashable, ...]:
    tmp = list(items)
    tmp.sort()
    return tuple(tmp)


class Partitions(NamedTuple):
    left: FrozenSet[Hashable]
    right: FrozenSet[Hashable]


def binary_partition(superset: Set[Hashable],) -> Set[Partitions]:
    if len(superset) < 2:
        raise ValueError("Superset must contain at least two elements")
    res: Set[Partitions] = set()
    for k in range(1, len(superset)):
        for c in combinations(superset, k):
            left = frozenset(c)
            right = frozenset(superset - left)
            res.add(Partitions(left, right))
    return res


class Pair(NamedTuple):
    basket_id: Hashable
    item_id: Hashable


def frequent_itemsets(
    pairs: Iterable[Pair], minsup: float, k: int
) -> List[List[Itemset]]:
    """Apriori algorithm to generate frequent k-itemsets.

    :param pairs: Pairs of (basket id, item id)
    :param minsup: Minimum support
    :param k: maximum size of itemset
    :return: List of Itemsets sorted by support count in descending order.
    """
    if k < 1:
        raise ValueError("k must not be less than 1")
    res: List[List[Itemset]] = [[] for _ in range(k)]
    bids: Set[Hashable] = set()
    index: DefaultDict[Hashable, Set[Hashable]] = defaultdict(set)
    for p in pairs:
        bids.add(p.basket_id)
        index[p.item_id].add(p.basket_id)
    n = len(bids)
    threshold = minsup * n
    for item, baskets in index.items():  # Time O(N)
        support_count = len(baskets)
        if support_count >= threshold:
            res[0].append(Itemset(support_count=support_count, items={item}))
    for kth in range(2, k + 1):  # Time O(KN)
        pool: Set[Hashable] = set()
        for iset in res[kth - 2]:
            pool = pool | iset.items
        for items in combinations(pool, kth):
            baskets = index[items[0]]
            for i in range(1, len(items)):
                baskets = baskets & index[items[i]]
            support_count = len(baskets)
            if support_count >= threshold:
                res[kth - 1].append(
                    Itemset(support_count=support_count, items=set(items))
                )
    for r in res:  # Time O(K * N lg N)
        r.sort(reverse=True)
    return res
