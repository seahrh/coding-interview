from collections import defaultdict, deque
from typing import (
    TypeVar,
    Generic,
    DefaultDict,
    Set,
    List,
    Callable,
    Deque,
    Tuple,
    FrozenSet,
)

T = TypeVar("T")  # Declare type variable


class Graph(Generic[T]):
    """ Graph data structure, undirected by default. """

    def __init__(self, directed: bool = False):
        # adjacency list: using a Set instead of List (assume all vertices are distinct).
        self._alist: DefaultDict[T, Set[T]] = defaultdict(set)
        self._directed: bool = directed

    def nodes(self) -> FrozenSet[T]:
        return frozenset(self._alist.keys())

    def add_nodes(self, *nodes: T) -> None:
        """Add an unconnected node."""
        for node in nodes:
            self._alist[node] = set()

    def add(self, *edges: Tuple[T, T]) -> None:
        """ Add edges (list of tuple pairs) to graph """
        for left, right in edges:
            self._alist[left].add(right)
            if not self._directed:
                self._alist[right].add(left)

    def remove_nodes(self, *nodes: T) -> None:
        """ Remove all references to node """
        for node in nodes:
            for neighbours in self._alist.values():
                if node in neighbours:
                    neighbours.remove(node)
            if node in self._alist:
                del self._alist[node]

    def remove(self, *edges: Tuple[T, T]) -> None:
        for left, right in edges:
            if left in self._alist:
                self._alist[left].remove(right)
                if not self._directed and right in self._alist:
                    self._alist[right].remove(left)

    def is_adjacent(self, from_node: T, to_node: T) -> bool:
        """ Is node1 directly connected to node2 """
        return from_node in self._alist and to_node in self._alist[from_node]

    def adjacent(self, node: T) -> FrozenSet[T]:
        return frozenset(self._alist[node])

    def connected_component(self, node: T, visited: Set[T] = None) -> Set[T]:
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
            res = res | self.connected_component(n, visited)  # set union
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
