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
            for a in self.adjacent(curr):
                if a not in discovered:
                    discovered.add(a)
                    st.append(a)
        return res

    def find_cycle(self) -> "DiGraph[T]":
        """Returns one cycle in the graph if it exists.
        Explored means that a node and all its descendants have been explored.
        White set: nodes that have not been explored
        Gray set: nodes that are undergoing exploration but not completed
        Black set: nodes that are completely explored

        Time O(V + E): same as DFS
        Space O(V): stack covers all nodes
        Based on https://www.youtube.com/watch?v=rKQaZuoUR4M
        """
        res: "DiGraph[T]" = DiGraph[T]()
        white: Set[T] = set(self.nodes())
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
            for a in self.adjacent(curr):
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

    def has_cycle(self) -> bool:
        return len(self.find_cycle()) != 0

    def topsort(self) -> List[T]:
        """Topological sort orders the vertices on a line such that all directed edges go from left to right.

        Time O(V + E): DFS traversal
        Space O(V)
        """
        ordering: Deque[T] = deque()  # result is a queue; insert from left
        st: List[T] = []  # DFS iteration
        white: Set[T] = set(self.nodes())
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
            for a in self.adjacent(curr):
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
