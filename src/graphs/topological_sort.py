"""
Find Cycles
=============
Returns one cycle in the graph if it exists.
Explored means that a node and all its descendants have been explored.
White set: nodes that have not been explored
Gray set: nodes that are undergoing exploration but not completed
Black set: nodes that are completely explored

Time O(V + E): same as DFS
Space O(V): stack covers all nodes
Based on https://www.youtube.com/watch?v=rKQaZuoUR4M


Topological Sort
==================
Topological sort orders the vertices on a line such that all directed edges go from left to right.
Time O(V + E): DFS traversal
Space O(V)
"""
from collections import deque
from typing import Deque, Dict, List, Optional, Set

from graphs.graph import DiGraph, Edge, T


def find_cycle(graph: DiGraph[T]) -> DiGraph[T]:
    res: DiGraph[T] = DiGraph[T]()
    white: Set[T] = set(graph.nodes())
    gray: Set[T] = set()
    black: Set[T] = set()
    st: List[T] = []  # dfs
    parent: Dict[T, Optional[T]] = {}  # map of child node to parent node
    while len(white) != 0 or len(st) != 0:
        if len(st) == 0:
            # add next node from white set
            # both white set and stack cannot be empty at the same time.
            tmp = white.pop()
            gray.add(tmp)
            st.append(tmp)
            parent[tmp] = None
        curr = st[-1]  # do not pop the top!
        explored = True
        for a in graph.adjacent(curr):
            if a in black:
                continue
            if a in gray:  # cycle found
                left: Optional[T] = curr
                right: T = a
                while left is not None:
                    res.add(Edge(left, right))
                    right = left
                    left = parent[left]
                return res
            explored = False
            parent[a] = curr
            white.discard(a)
            gray.add(a)
            st.append(a)
        if explored:
            st.pop()  # pop only if the node and its successors have been explored
            gray.remove(curr)
            black.add(curr)
    return res


def has_cycle(graph: DiGraph[T]) -> bool:
    return len(find_cycle(graph)) != 0


def topsort(graph: DiGraph[T]) -> List[T]:
    ordering: Deque[T] = deque()  # result is a queue; insert from left
    st: List[T] = []  # DFS iteration
    white: Set[T] = set(graph.nodes())
    gray: Set[T] = set()
    black: Set[T] = set()
    while len(white) != 0 or len(st) != 0:
        if len(st) == 0:
            # add next node from white set
            # both white set and stack cannot be empty at the same time.
            tmp = white.pop()
            gray.add(tmp)
            st.append(tmp)
        curr = st[-1]  # do not pop the top!
        explored = True
        for a in graph.adjacent(curr):
            if a in black:
                continue
            if a in gray:  # cycle found; topological sort is not possible
                return []
            explored = False
            white.discard(a)
            gray.add(a)
            st.append(a)
        if explored:
            st.pop()  # pop only if the node and its successors have been explored
            gray.remove(curr)
            black.add(curr)
            ordering.appendleft(curr)
    return list(ordering)
