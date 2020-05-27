from collections import defaultdict, deque
from typing import (
    TypeVar,
    Generic,
    DefaultDict,
    Set,
    List,
    Callable,
    Deque,
    KeysView,
    Iterable,
    Tuple,
)

T = TypeVar("T")  # Declare type variable


class Graph(Generic[T]):
    """ Graph data structure, undirected by default. """

    def __init__(self, directed: bool = False):
        # adjacency list: using a Set instead of a List
        # because we assume all vertices are distinct.
        self._alist: DefaultDict[T, Set[T]] = defaultdict(set)
        self._directed: bool = directed

    def nodes(self) -> KeysView[T]:
        return self._alist.keys()

    def add_node(self, node: T) -> None:
        """ Add an unconnected node. This allows unconnected components. """
        self._alist[node] = set()

    def add_edge(self, node1: T, node2: T) -> None:
        """ Add connection between node1 and node2 """
        self._alist[node1].add(node2)
        if not self._directed:
            self._alist[node2].add(node1)

    def add_nodes(self, nodes: Iterable[T]):
        for n in nodes:
            self.add_node(n)

    def add_edges(self, edges: Iterable[Tuple[T, T]]):
        """ Add edges (list of tuple pairs) to graph """
        for node1, node2 in edges:
            self.add_edge(node1, node2)

    def remove(self, node: T) -> None:
        """ Remove all references to node """
        for neighbours in self._alist.values():
            if node in neighbours:
                neighbours.remove(node)
        if node in self._alist:
            del self._alist[node]

    def is_adjacent(self, from_node: T, to_node: T) -> bool:
        """ Is node1 directly connected to node2 """
        return from_node in self._alist and to_node in self._alist[from_node]

    def adjacent(self, node: T) -> Set[T]:
        return self._alist[node]

    def component(self, node: T, visited: Set[T] = None) -> Set[T]:
        """Returns all nodes in the same connected component as the input node.
        O(n) time and O(n) space, where n is the size of the component."""
        if node not in self._alist:
            return set()
        if visited is None:
            visited = set()
        if node in visited:
            return set()
        res = {node}
        visited.add(node)
        for n in self.adjacent(node):
            res = res | self.component(n, visited)  # set union
        return res

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, dict(self._alist))


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
