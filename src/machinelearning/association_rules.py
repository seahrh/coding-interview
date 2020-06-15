from itertools import combinations
from typing import NamedTuple, Union, Set, Iterable, Tuple, FrozenSet

Identifier = Union[int, str]


class Itemset(NamedTuple):
    support_count: int
    items: Set[Identifier]


class Rule(NamedTuple):
    confidence: float
    support: float
    antecedent: Itemset
    consequent: Itemset


def _key(items: Iterable[Identifier]) -> Tuple[Identifier, ...]:
    tmp = list(items)
    tmp.sort()
    return tuple(tmp)


class Partitions(NamedTuple):
    left: FrozenSet[Identifier]
    right: FrozenSet[Identifier]


def binary_partition(superset: Set[Identifier],) -> Set[Partitions]:
    if len(superset) < 2:
        raise ValueError("Superset must contain at least two elements")
    res: Set[Partitions] = set()
    for k in range(1, len(superset)):
        for c in combinations(superset, k):
            left = frozenset(c)
            right = frozenset(superset - left)
            res.add(Partitions(left, right))
    return res
