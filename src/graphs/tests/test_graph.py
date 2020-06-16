from graphs.graph import *


class TestGraph:
    def test_undirected_graph(self):
        g = Graph[int](directed=False)
        g.add_nodes(1, 2, 3, 4)
        assert g.adjacent(1) == g.adjacent(2) == g.adjacent(3) == g.adjacent(4) == set()
        g.add((1, 2), (2, 3), (3, 4), (4, 1))
        assert g.adjacent(1) == {2, 4}
        assert g.adjacent(2) == {3, 1}
        assert g.adjacent(3) == {2, 4}
        assert g.adjacent(4) == {1, 3}
        g.remove_nodes(1, 2)
        assert g.nodes() == {3, 4}
        assert g.adjacent(3) == {4} and g.adjacent(4) == {3}
        g.remove((3, 4))
        assert g.nodes() == {3, 4}
        assert g.adjacent(3) == g.adjacent(4) == set()


class TestBreadthFirstSearch:
    def test_bfs(self):
        g = Graph[int]()
        g.add_nodes(1)
        assert bfs(g, start_node=1) == [1]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7))
        assert bfs(g, start_node=1) == [1, 2, 3, 4, 5, 6, 7]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 8), (6, 9))
        assert bfs(g, start_node=1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestDepthFirstSearch:
    def test_dfs(self):
        g = Graph[int]()
        g.add_nodes(1)
        assert dfs(g, start_node=1) == [1]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7))
        assert dfs(g, start_node=1) == [1, 3, 7, 6, 2, 5, 4]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 8), (6, 9))
        assert dfs(g, start_node=1) == [1, 3, 7, 6, 9, 2, 5, 8, 4]
