"""
Depth first search method to find the connected component of a given node.
This method works only for undirected graphs.
Time O(V + E)
Space O(V + E)
"""
from typing import Set

from codi.graphs.graph import Edge, Graph, T


def _component(graph: Graph[T], node: T, result: Graph[T], visited: Set[T]) -> None:
    if node not in graph:
        return
    # base case: node already visited
    # cannot use result.nodes() because edges are added in both directions.
    if node in visited:
        return
    visited.add(node)
    result.add_nodes(node)  # node may not have edges
    for a in graph.adjacent(node):
        result.add(Edge(node, a))
        _component(graph, a, result, visited)


def component(graph: Graph[T], node: T) -> Graph[T]:
    """Returns the connected component that contains the given vertex, as a new Graph object.
    A vertex with no incident edges is itself a component.
    A graph that is itself connected has exactly one component, consisting of the whole graph.
    """
    res: Graph = Graph()
    _component(graph, node, res, visited=set())
    return res


def components(graph: Graph[T]) -> Set[Graph[T]]:
    res: Set[Graph[T]] = set()
    seen: Set[T] = set()
    for node in graph.nodes():
        if node in seen:
            continue
        c = component(graph, node)
        res.add(c)
        seen = seen | c.nodes()
    return res
