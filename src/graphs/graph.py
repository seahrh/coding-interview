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
)

T = TypeVar("T", bound=Hashable)  # Declare type variable


class Edge(Generic[T]):
    """Directed edge going from left node to right node."""

    def __init__(self, left: T, right: T, weight: float = 0, label: str = ""):
        self.left = left
        self.right = right
        self.weight = weight
        self.label = label

    def __tuple(self) -> Tuple[Hashable, ...]:
        return self.left, self.right, self.weight, self.label

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__tuple() == other.__tuple()
        return False

    def __hash__(self):
        return hash(self.__tuple())

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.__dict__)


class DiGraph(Generic[T]):
    """ Directed Graph data structure"""

    def __init__(self):
        # Adjacency list: use a Dict or Set instead of List (assume all vertices are distinct).
        # For weighted graphs, ALIST is represented as a nested hash table: left node -> right node -> Edge
        # For unweighted graphs, ALIST is represented as a hash table: left node -> Set of right nodes
        self._alist: DefaultDict[T, Dict[T, Edge[T]]] = defaultdict(dict)

    def is_adjacent(self, from_node: T, to_node: T) -> bool:
        """ Is node1 directly connected to node2 """
        return from_node in self._alist and to_node in self._alist[from_node]

    def adjacent(self, node: T) -> FrozenSet[T]:
        return frozenset(self._alist[node])

    def nodes(self) -> FrozenSet[T]:
        return frozenset(self._alist.keys())

    def edges(self) -> FrozenSet[Edge[T]]:
        res: Set[Edge[T]] = set()
        for edges in self._alist.values():
            for edge in edges.values():
                res.add(edge)
        return frozenset(res)

    def out_edges(self, node: T) -> FrozenSet[Edge[T]]:
        """Outgoing edges from the given node."""
        return frozenset(self._alist[node].values())

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

    def __contains__(self, item: T) -> bool:
        return item in self._alist

    def add_nodes(self, *nodes: T) -> None:
        """Add an unconnected node."""
        for node in nodes:
            self._alist[node] = {}

    def remove_nodes(self, *nodes: T) -> None:
        """ Remove all references to node """
        for node in nodes:
            for edges in self._alist.values():
                if node in edges:
                    del edges[node]
            if node in self._alist:
                del self._alist[node]

    def add(self, *edges: Edge[T]) -> None:
        """ Add edges (list of tuple pairs) to graph """
        for edge in edges:
            self._alist[edge.left][edge.right] = edge
            if edge.right not in self._alist:  # add new node
                self._alist[edge.right] = {}

    def remove(self, *edges: Edge[T]) -> None:
        for edge in edges:
            if edge.left in self._alist and edge.right in self._alist[edge.left]:
                del self._alist[edge.left][edge.right]

    def bfs(self, start_node: T, process: Callable[[T], None] = None) -> List[T]:
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
            for a in self.adjacent(curr):
                if a not in discovered:
                    discovered.add(a)
                    q.append(a)
        return res

    def dfs(self, start_node: T, process: Callable[[T], None] = None) -> List[T]:
        """Returns the path of nodes visited in Depth First Search.
        Uses a stack to pick the next node to process.
        Time O(V + E)
        Space O(V)
        """
        st: List[T] = []
        discovered: Set[T] = set()
        res: List[T] = []
        st.append(start_node)
        discovered.add(start_node)
        while len(st) != 0:
            curr = st.pop()
            res.append(curr)
            if process is not None:
                process(curr)
            for a in self.adjacent(curr):
                if a not in discovered:
                    discovered.add(a)
                    st.append(a)
        return res

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, dict(self._alist))


class Graph(DiGraph, Generic[T]):
    """Undirected graph, as a special case of a directed graph."""

    def add(self, *edges: Edge[T]) -> None:
        super().add(*edges)
        for edge in edges:
            self._alist[edge.right][edge.left] = Edge(
                edge.right, edge.left, weight=edge.weight, label=edge.label
            )

    def remove(self, *edges: Edge[T]) -> None:
        super().remove(*edges)
        for edge in edges:
            if edge.right in self._alist and edge.left in self._alist[edge.right]:
                del self._alist[edge.right][edge.left]
