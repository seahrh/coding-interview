"""
0/1 Knapsack Problem
======================
Given weights and values of N items, put these items in a knapsack of capacity C
to get the maximum total value in the knapsack.
You cannot divide an item, either pick the whole item or don’t pick it (0-1 property).
A single solution is expressed as an boolean array that indicates whether the item is present in the knapsack.
Find all solutions.

SOLUTION: Least cost branch and bound
LC BB seeks the lowest cost so turn the problem into minimization with negative values.
Time O(2^N lg 2^N): expand almost all nodes in worst case. Heap insert time is O(lg N).
Space O(2^N): state space tree as min-heap.

Based on https://www.youtube.com/watch?v=yV1d-b_NeK8
"""

from heapq import heappop, heappush
from typing import List, NamedTuple, Set, Tuple, Union

Numeric = Union[int, float]


class Node(NamedTuple):
    cost: float
    upper: float
    weight: float
    partial: Tuple[bool, ...]


class LeastCostTree:
    def __init__(
        self,
        capacity: Numeric,
        weights: List[Numeric],
        values: List[Numeric],
        best_upper: float = 0,
    ):
        self.capacity = capacity
        self.weights = weights
        self.values = values
        self.best_upper = best_upper
        self.min_heap: List[Node] = []

    def __len__(self):
        return len(self.min_heap)

    def push(self, partial: List[bool]) -> None:
        cost: float = 0
        upper: float = 0
        weight: float = 0
        for i in range(len(self.weights)):
            must_include = False
            if i < len(partial):
                if not partial[i]:  # item is not in the bag
                    continue
                must_include = True
            if weight + self.weights[i] > self.capacity:
                # solution is not feasible as the item cannot fit in the bag
                if must_include:
                    return
                remainder = self.capacity - weight
                # take fraction: fill remaining capacity with "price per pound" of current item
                cost -= self.values[i] / self.weights[i] * remainder
                break
            weight += self.weights[i]
            upper -= self.values[i]
            cost = upper
        # at least one item is picked
        if upper > self.best_upper and any(partial):
            return
        if upper < self.best_upper:
            self.best_upper = upper
        node = Node(partial=tuple(partial), weight=weight, cost=cost, upper=upper)
        heappush(self.min_heap, node)

    def pop(self) -> Node:
        return heappop(self.min_heap)

    def __repr__(self):
        return f"""{self.__class__.__name__}(
    best_upper={self.best_upper},
    min_heap={repr(self.min_heap)},
    capacity={self.capacity}
)
"""


def knapsack(
    capacity: Numeric, weights: List[Numeric], values: List[Numeric]
) -> Set[Tuple[bool, ...]]:
    if len(weights) == 0:
        raise ValueError("Weights array must not be empty")
    if len(values) == 0:
        raise ValueError("Values array must not be empty")
    if len(weights) != len(values):
        raise ValueError("Both weights and values arrays must have equal length")
    tree = LeastCostTree(capacity, weights, values)
    tree.push(partial=[True])
    tree.push(partial=[False])
    candidates: Set[Node] = set()
    while len(tree) != 0:
        # get the least cost node
        node: Node = tree.pop()
        if len(node.partial) == len(weights):
            candidates.add(node)
            continue
        partial = list(node.partial)
        tree.push(partial=partial + [True])
        tree.push(partial=partial + [False])
    res: Set[Tuple[bool, ...]] = set()
    for c in candidates:
        if c.upper == tree.best_upper:
            res.add(c.partial)
    return res
