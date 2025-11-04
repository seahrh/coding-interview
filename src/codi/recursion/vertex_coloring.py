"""
M Coloring Decision Problem
==============================
Given an undirected graph and a number m, determine if the graph can be coloured with at most m colours
such that no two adjacent vertices of the graph are colored with the same color.
Here coloring of a graph means the assignment of colors to all vertices.

Input:
A 2D array graph[V][V] where V is the number of vertices in graph
and graph[V][V] is adjacency matrix representation of the graph.
A value graph[i][j] is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0.
An integer m which is the maximum number of colors that can be used.

Output:
All possible coloring arrangements; return a Set of Tuples.
Each tuple is an array color[V] that should have numbers from 1 to m.
color[i] should represent the color assigned to the ith vertex.
The code should also return empty Set if the graph cannot be colored with m colors.

See https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/

SOLUTION: Backtracking

Time O(M^V)
Space O(V): recursive call stack, store the result.
"""

from typing import List, Set, Tuple


def _is_complete(graph: List[List[bool]], partial: List[int]) -> bool:
    for i in range(len(partial)):
        if partial[i] == 0:
            return False
        for j, is_neighbour in enumerate(graph[i]):
            if is_neighbour and partial[i] == partial[j]:
                return False
    return True


def _vertex_coloring(
    graph: List[List[bool]],
    m: int,
    vertex: int,
    partial: List[int],
    result: Set[Tuple[int, ...]],
) -> None:
    print(f"vertex={vertex}, partial={partial}, result={result}")
    color = partial[vertex]
    for i, is_neighbor in enumerate(graph[vertex]):
        if not is_neighbor:  # simple graph; no self loops else coloring is impossible
            continue
        print(f"i={i}")
        # this check must come next in order
        # bounding function: neighbor must not have the same color.
        if partial[i] == color:
            return
        if partial[i] != 0:  # color already assigned
            continue
        # No branching if solution is complete
        for c in range(1, m + 1):
            if c != color:
                partial[i] = c
                _vertex_coloring(graph, m, i, partial, result)
    # base case: all vertices assigned correctly; complete solution
    if _is_complete(graph, partial):
        result.add(tuple(partial))


def vertex_coloring(graph: List[List[bool]], m: int) -> Set[Tuple[int, ...]]:
    if graph is None or len(graph) == 0:
        raise ValueError("Graph must not be None or empty")
    if m < 1:
        raise ValueError("Number of colors m must be at least 1.")
    res: Set[Tuple[int, ...]] = set()
    for color in range(1, m + 1):
        partial = [0] * len(graph)
        partial[0] = color
        _vertex_coloring(graph, m, vertex=0, partial=partial, result=res)
    return res
