from collections import defaultdict
from itertools import combinations
from typing import (
    DefaultDict,
    Dict,
    FrozenSet,
    Hashable,
    Iterable,
    List,
    NamedTuple,
    Set,
    Tuple,
)


class Itemset(NamedTuple):
    support_count: int
    items: Set[Hashable]


class Rule(NamedTuple):
    confidence: float
    support: float
    antecedent: FrozenSet[Hashable]
    consequent: FrozenSet[Hashable]


def _key(items: Iterable[Hashable]) -> Tuple[Hashable, ...]:
    tmp = list(items)
    tmp.sort()
    return tuple(tmp)


class Partitions(NamedTuple):
    left: FrozenSet[Hashable]
    right: FrozenSet[Hashable]


def binary_partition(
    superset: Set[Hashable],
) -> Set[Partitions]:
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


def baskets(pairs: Iterable[Pair]) -> Set[Hashable]:
    bids: Set[Hashable] = set()
    for p in pairs:
        bids.add(p.basket_id)
    return bids


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
    n = len(baskets(pairs))
    threshold = minsup * n
    # Index of item id to its containing set of basket ids
    index: DefaultDict[Hashable, Set[Hashable]] = defaultdict(set)
    for p in pairs:
        index[p.item_id].add(p.basket_id)
    for item, basket_ids in index.items():  # Time O(N)
        support_count = len(basket_ids)
        if support_count >= threshold:
            res[0].append(Itemset(support_count=support_count, items={item}))
    for kth in range(2, k + 1):  # Time O(KN)
        pool: Set[Hashable] = set()
        for iset in res[kth - 2]:
            pool = pool | iset.items
        for items in combinations(pool, kth):
            basket_ids = index[items[0]]
            for i in range(1, len(items)):
                basket_ids = basket_ids & index[items[i]]
            support_count = len(basket_ids)
            if support_count >= threshold:
                res[kth - 1].append(
                    Itemset(support_count=support_count, items=set(items))
                )
    for r in res:  # Time O(K * N lg N)
        r.sort(reverse=True)
    return res


def rules(pairs: Iterable[Pair], minsup: float, k: int, minconf: float) -> List[Rule]:
    """Generates association rules pruned by minimum support and confidence.

    :param pairs: Pairs of (basket id, item id)
    :param minsup: Minimum support
    :param k: maximum size of itemset
    :param minconf:
    :return: List of Rules sorted by confidence score in descending order.
    """
    res: List[Rule] = []
    n = len(baskets(pairs))
    fis = frequent_itemsets(pairs, minsup, k)
    support_counts: Dict[Tuple[Hashable, ...], int] = {}
    for fis_k in fis:
        for itemset in fis_k:
            support_counts[_key(itemset.items)] = itemset.support_count
    # skip 1-itemsets because rules require at least 2-itemsets
    for i in range(1, len(fis)):
        for itemset in fis[i]:
            for p in binary_partition(itemset.items):
                num = support_counts[_key(itemset.items)]
                c: float = num / support_counts[_key(p.left)]
                s: float = num / n
                if c >= minconf:
                    res.append(
                        Rule(
                            confidence=c,
                            support=s,
                            antecedent=p.left,
                            consequent=p.right,
                        )
                    )
    res.sort(reverse=True)
    return res
