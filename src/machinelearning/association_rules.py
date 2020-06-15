from itertools import combinations
from typing import NamedTuple, Set, Iterable, Tuple, FrozenSet, Hashable


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
