from codi.graphs.graph import *


class TestGraphs:
    def test_directed_graph(self):
        g = DiGraph[int]()
        g.remove_nodes(1)  # delete non-existent node
        g.add_nodes(1, 2, 3, 4)
        assert 1 in g and 2 in g and 3 in g and 4 in g
        assert g.adjacent(1) == g.adjacent(2) == g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(1, 2)
        edges = [Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(4, 1)]
        g.add(*edges)
        assert g.nodes() == {1, 2, 3, 4}
        assert g.edges() == set(edges)
        assert g.adjacent(1) == {2} and g.is_adjacent(1, 2) and not g.is_adjacent(2, 1)
        assert g.adjacent(2) == {3} and g.is_adjacent(2, 3) and not g.is_adjacent(3, 2)
        assert g.adjacent(3) == {4} and g.is_adjacent(3, 4) and not g.is_adjacent(4, 3)
        assert g.adjacent(4) == {1} and g.is_adjacent(4, 1) and not g.is_adjacent(1, 4)
        g.remove_nodes(1, 2)
        assert g.nodes() == {3, 4}
        assert 3 in g and 4 in g
        assert g.edges() == {Edge(3, 4)}
        assert g.adjacent(3) == {4} and g.is_adjacent(3, 4)
        assert g.adjacent(4) == set() and not g.is_adjacent(4, 3)
        g.remove(Edge(4, 3))  # delete non-existent edge
        assert g.nodes() == {3, 4}
        assert 3 in g and 4 in g
        assert g.edges() == {Edge(3, 4)}
        assert g.adjacent(3) == {4} and g.is_adjacent(3, 4)
        g.remove(Edge(3, 4))
        assert g.nodes() == {3, 4}
        assert 3 in g and 4 in g
        assert g.edges() == set()
        assert g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(3, 4)

    def test_undirected_graph(self):
        g = Graph[int]()
        g.remove_nodes(1)  # delete non-existent node
        g.add_nodes(1, 2, 3, 4)
        assert 1 in g and 2 in g and 3 in g and 4 in g
        assert g.adjacent(1) == g.adjacent(2) == g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(1, 2)
        g.remove(Edge(1, 2))  # delete non-existent edge
        g.add(Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(4, 1))
        assert g.nodes() == {1, 2, 3, 4}
        assert g.edges() == {
            Edge(1, 2),
            Edge(2, 1),
            Edge(2, 3),
            Edge(3, 2),
            Edge(3, 4),
            Edge(4, 3),
            Edge(4, 1),
            Edge(1, 4),
        }
        assert g.adjacent(1) == {2, 4} and g.is_adjacent(1, 2) and g.is_adjacent(1, 4)
        assert g.adjacent(2) == {3, 1} and g.is_adjacent(2, 3) and g.is_adjacent(1, 2)
        assert g.adjacent(3) == {2, 4} and g.is_adjacent(3, 2) and g.is_adjacent(3, 4)
        assert g.adjacent(4) == {1, 3} and g.is_adjacent(1, 4) and g.is_adjacent(3, 4)
        g.remove_nodes(1, 2)
        assert g.nodes() == {3, 4}
        assert 3 in g and 4 in g
        assert g.edges() == {Edge(3, 4), Edge(4, 3)}
        assert g.adjacent(3) == {4} and g.is_adjacent(4, 3)
        assert g.adjacent(4) == {3} and g.is_adjacent(4, 3)
        g.remove(Edge(3, 4))
        assert g.nodes() == {3, 4}
        assert 3 in g and 4 in g
        assert g.edges() == set()
        assert g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(3, 4)


class TestBreadthFirstSearch:
    def test_bfs(self):
        g = Graph[int]()
        g.add_nodes(1)
        assert g.bfs(start_node=1) == [1]
        g = Graph[int]()
        g.add(Edge(1, 2), Edge(1, 3), Edge(2, 4), Edge(2, 5), Edge(3, 6), Edge(3, 7))
        assert g.bfs(start_node=1) == [1, 2, 3, 4, 5, 6, 7]
        g = Graph[int]()
        g.add(
            Edge(1, 2),
            Edge(1, 3),
            Edge(2, 4),
            Edge(2, 5),
            Edge(3, 6),
            Edge(3, 7),
            Edge(5, 8),
            Edge(6, 9),
        )
        assert g.bfs(start_node=1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestDepthFirstSearch:
    def test_dfs(self):
        g = Graph[int]()
        g.add_nodes(1)
        assert g.dfs(start_node=1) == [1]
        g = Graph[int]()
        g.add(Edge(1, 2), Edge(1, 3), Edge(2, 4), Edge(2, 5), Edge(3, 6), Edge(3, 7))
        assert g.dfs(start_node=1) == [1, 3, 7, 6, 2, 5, 4]
        g = Graph[int]()
        g.add(
            Edge(1, 2),
            Edge(1, 3),
            Edge(2, 4),
            Edge(2, 5),
            Edge(3, 6),
            Edge(3, 7),
            Edge(5, 8),
            Edge(6, 9),
        )
        assert g.dfs(start_node=1) == [1, 3, 7, 6, 9, 2, 5, 8, 4]
