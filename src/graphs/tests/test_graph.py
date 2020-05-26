from graphs.graph import *


class TestBreadthFirstSearch:
    def test_bfs(self):
        g = Graph[int]()
        g.add_node(1)
        assert bfs(g, start_node=1) == [1]
        g = Graph[int]()
        g.add_edges([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
        assert bfs(g, start_node=1) == [1, 2, 3, 4, 5, 6, 7]
        g = Graph[int]()
        g.add_edges([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 8), (6, 9)])
        assert bfs(g, start_node=1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
