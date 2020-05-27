from collections import defaultdict, deque
from typing import TypeVar, Generic, DefaultDict, Set, List, Callable, Deque

T = TypeVar("T")  # Declare type variable


class Graph(Generic[T]):
    """ Graph data structure, undirected by default. """

    def __init__(self, directed: bool = False):
        self._graph: DefaultDict[T, Set[T]] = defaultdict(set)
        self._directed: bool = directed

    def nodes(self):
        return self._graph.keys()

    def add_node(self, node):
        """ Add an unconnected node. This allows unconnected components. """
        self._graph[node] = set()

    def add_edge(self, node1, node2):
        """ Add connection between node1 and node2 """
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def add_nodes(self, nodes):
        for n in nodes:
            self.add_node(n)

    def add_edges(self, edges):
        """ Add edges (list of tuple pairs) to graph """
        for node1, node2 in edges:
            self.add_edge(node1, node2)

    def remove(self, node):
        """ Remove all references to node """
        for neighbours in self._graph.values():
            if node in neighbours:
                neighbours.remove(node)
        if node in self._graph:
            del self._graph[node]

    def is_adjacent(self, from_node, to_node):
        """ Is node1 directly connected to node2 """
        return from_node in self._graph and to_node in self._graph[from_node]

    def adjacent(self, node):
        return self._graph[node]

    def component(self, node: T, visited=None) -> Set[T]:
        """O(n) time and O(n) space, where n is the size of the component."""
        if node not in self._graph:
            return set()
        if visited is None:
            visited = set()
        if node in visited:
            return set()
        res = {node}
        visited.add(node)
        for n in self.adjacent(node):
            res = res | self.component(n, visited)
        return res

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, dict(self._graph))


def bfs(graph: Graph[T], start_node: T, process: Callable[[T], None] = None) -> List[T]:
    """Returns the path of nodes visited in Breadth First Search.
    Uses a queue to pick the next node to process.
    Time O(V + E)
    Space O(V)
    """
    q: Deque[T] = deque()
    discovered: Set[T] = set()
    res: List[T] = []
    q.append(start_node)
    discovered.add(start_node)
    while len(q) != 0:
        curr = q.popleft()
        res.append(curr)
        if process is not None:
            process(curr)
        for neighbour in graph.adjacent(curr):
            if neighbour not in discovered:
                discovered.add(neighbour)
                q.append(neighbour)
    return res


def dfs(graph: Graph[T], start_node: T, process: Callable[[T], None] = None) -> List[T]:
    """Returns the path of nodes visited in Depth First Search.
    Uses a stack to pick the next node to process.
    Time O(V + E)
    Space O(V)
    """
    st: Deque[T] = deque()
    discovered: Set[T] = set()
    res: List[T] = []
    st.append(start_node)
    discovered.add(start_node)
    while len(st) != 0:
        curr = st.pop()
        res.append(curr)
        if process is not None:
            process(curr)
        for neighbour in graph.adjacent(curr):
            if neighbour not in discovered:
                discovered.add(neighbour)
                st.append(neighbour)
    return res
