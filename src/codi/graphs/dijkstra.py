"""
============================================================
Dijkstra algorithm for finding single-source shortest path
============================================================
Given a directed graph and a source vertex in the graph,
the task is to find the shortest distance and path from source to target vertex in the given graph
where edges are weighted (non-negative).

SOLUTION: Greedy BFS using a min heap instead of queue

- Mark all vertices unvisited. Create a set of all unvisited vertices.
- Assign zero distance value to source vertex and infinity distance value to all other vertices.
- Set the source vertex as current vertex
- For current vertex, consider all of its unvisited children
and calculate their tentative distances through the current. (distance of current + weight of the corresponding edge)
- Compare the newly calculated distance to the current assigned value (can be infinity for some vertices)
and assign the smaller one.
- After considering all the unvisited children of the current vertex, mark the current as visited
and remove it from the unvisited set.
- Similarly, continue for all the vertex until all the nodes are visited.

Time O((V + E) lg V): BFS takes O(V + E) steps and at each step, heap insert in O(lg V).
Space O(V): maintain Unvisited set and to store the result

Cons
- Cannot be used on edges with negative weights
- Evaluate all nodes, unlike A*

See
- https://www.youtube.com/watch?v=XB4MIexjvY0
"""

import sys
from heapq import heappop, heappush
from typing import Dict, List, Optional, Set, Tuple

from codi.graphs.graph import DiGraph, T


class Distance:
    def __init__(self, cost: float, child: T, parent: Optional[T] = None):
        self.cost = cost
        self.child = child
        self.parent = parent

    def __tuple(self) -> Tuple:
        return self.cost, self.child, self.parent

    def __eq__(self, other):
        if type(self) is type(other):
            return self.__tuple() == other.__tuple()
        return False

    def __hash__(self):
        return hash(self.__tuple())

    def __lt__(self, other):
        return self.__tuple() < other.__tuple()

    def __repr__(self):
        return f"{__class__.__name__}({self.__dict__})"


def distances(
    graph: DiGraph, source: T, max_cost: int = sys.maxsize
) -> Dict[T, Distance]:
    if source not in graph:
        raise ValueError("Source node not found in the graph")
    unvisited: Set[T] = set(graph.nodes())
    res: Dict[T, Distance] = {}
    node: T
    for node in unvisited:
        res[node] = Distance(cost=max_cost, child=node)
    d: Distance = res[source]
    d.cost = 0
    min_heap: List[Distance] = []
    heappush(min_heap, d)
    while len(unvisited) != 0 or len(min_heap) != 0:
        if len(min_heap) == 0:
            node = unvisited.pop()
            heappush(min_heap, res[node])
        curr: T = heappop(min_heap).child  # type: ignore[assignment]
        if curr not in unvisited:
            continue
        for edge in graph.out_edges(curr):
            a = edge.right
            best = res[a]
            cost = res[curr].cost + edge.weight
            if cost < best.cost:
                best.cost = cost
                best.parent = curr  # type: ignore[assignment]
            heappush(min_heap, best)
        unvisited.remove(curr)
    return res
