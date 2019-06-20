from collections import defaultdict


class Graph:
    """ Graph data structure, undirected by default. """

    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

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

    def component(self, node, visited=None):
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
            res = res.union(self.component(n, visited))
        return res

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
