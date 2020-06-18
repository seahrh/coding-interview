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
    Hashable,
    Dict,
    Optional,
)

T = TypeVar("T", bound=Hashable)  # Declare type variable


class DiGraph(Generic[T]):
    """ Directed Graph data structure"""

    def __init__(self):
        # adjacency list: using a Set instead of List (assume all vertices are distinct).
        self._alist: DefaultDict[T, Set[T]] = defaultdict(set)

    def is_adjacent(self, from_node: T, to_node: T) -> bool:
        """ Is node1 directly connected to node2 """
        return from_node in self._alist and to_node in self._alist[from_node]

    def adjacent(self, node: T) -> FrozenSet[T]:
        return frozenset(self._alist[node])

    def nodes(self) -> FrozenSet[T]:
        return frozenset(self._alist.keys())

    def edges(self) -> FrozenSet[Tuple[T, T]]:
        res: Set[Tuple[T, T]] = set()
        for left in self.nodes():
            for right in self.adjacent(left):
                res.add((left, right))
        return frozenset(res)

    def __tuple(self) -> Tuple[Hashable, ...]:
        return self.nodes(), self.edges()

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__tuple() == other.__tuple()
        return False

    def __hash__(self):
        return hash(self.__tuple())

    def __len__(self):
        return len(self.nodes())

    def add_nodes(self, *nodes: T) -> None:
        """Add an unconnected node."""
        for node in nodes:
            self._alist[node] = set()

    def remove_nodes(self, *nodes: T) -> None:
        """ Remove all references to node """
        for node in nodes:
            for neighbours in self._alist.values():
                neighbours.discard(node)
            if node in self._alist:
                del self._alist[node]

    def add(self, *edges: Tuple[T, T]) -> None:
        """ Add edges (list of tuple pairs) to graph """
        for left, right in edges:
            self._alist[left].add(right)

    def remove(self, *edges: Tuple[T, T]) -> None:
        for left, right in edges:
            if left in self._alist:
                self._alist[left].discard(right)

    def find_cycle(self) -> "DiGraph[T]":
        """Returns one cycle in the graph if it exists.

        Explored means that a node and all its descendants have been explored.

        Time O(V + E): same as DFS
        Space O(V): stack covers all nodes
        Based on https://www.youtube.com/watch?v=rKQaZuoUR4M
        """
        res: "DiGraph[T]" = DiGraph[T]()
        white: Set[T] = set(self.nodes())
        gray: Set[T] = set()
        black: Set[T] = set()
        st: List[T] = []  # dfs
        parent: Dict[T, Optional[T]] = {}
        while len(white) != 0 or len(st) != 0:
            if len(st) == 0:
                # completed exploring gray nodes, so flush to black set.
                black = black | gray
                gray = set()
                # add next node from white set
                # both white set and stack cannot be empty at the same time.
                tmp = white.pop()
                gray.add(tmp)
                st.append(tmp)
                parent[tmp] = None
            curr = st.pop()
            explored = True
            for a in self.adjacent(curr):
                if a in black:
                    continue
                if a in gray:  # cycle found
                    left: Optional[T] = curr
                    right: T = a
                    while left is not None:
                        res.add((left, right))
                        right = left
                        left = parent[left]
                    return res
                explored = False
                parent[a] = curr
                white.discard(a)
                gray.add(a)
                st.append(a)
            if explored:
                gray.remove(curr)
                black.add(curr)
        return res

    def has_cycle(self) -> bool:
        return len(self.find_cycle()) != 0

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, dict(self._alist))


class Graph(DiGraph, Generic[T]):
    """Undirected graph, as a special case of a directed graph."""

    def add(self, *edges: Tuple[T, T]) -> None:
        super().add(*edges)
        for left, right in edges:
            self._alist[right].add(left)

    def remove(self, *edges: Tuple[T, T]) -> None:
        super().remove(*edges)
        for left, right in edges:
            if right in self._alist:
                self._alist[right].discard(left)

    def _component(self, node: T, result: "Graph[T]", visited: Set[T]) -> None:
        """Depth first search method to find the connected component of a given node.
        This method works only for undirected graphs.
        Time O(V + E) and Space O(V + E)."""
        if node not in self.nodes():
            return
        # base case: node already visited
        # cannot use result.nodes() because edges are added in both directions.
        if node in visited:
            return
        visited.add(node)
        result.add_nodes(node)  # node may not have edges
        for a in self.adjacent(node):
            result.add((node, a))
            self._component(a, result, visited)

    def component(self, node: T) -> "Graph[T]":
        """Returns the connected component that contains the given vertex, as a new Graph object.
        A vertex with no incident edges is itself a component.
        A graph that is itself connected has exactly one component, consisting of the whole graph.
        """
        res = Graph[T]()
        self._component(node, res, visited=set())
        return res

    def components(self) -> "Set[Graph[T]]":
        res: Set[Graph[T]] = set()
        seen: Set[T] = set()
        for node in self.nodes():
            if node in seen:
                continue
            c = self.component(node)
            res.add(c)
            seen = seen | c.nodes()
        return res


def bfs(
    graph: DiGraph[T], start_node: T, process: Callable[[T], None] = None
) -> List[T]:
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


def dfs(
    graph: DiGraph[T], start_node: T, process: Callable[[T], None] = None
) -> List[T]:
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
