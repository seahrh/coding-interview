import pytest
from graphs.graph import *


class TestGraph:
    def test_undirected_graph(self):
        g = Graph[int](directed=False)
        g.remove_nodes(1)  # delete non-existent node
        g.add_nodes(1, 2, 3, 4)
        assert g.adjacent(1) == g.adjacent(2) == g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(1, 2)
        g.remove((1, 2))  # delete non-existent edge
        g.add((1, 2), (2, 3), (3, 4), (4, 1))
        assert g.edges() == {
            (1, 2),
            (2, 1),
            (2, 3),
            (3, 2),
            (3, 4),
            (4, 3),
            (4, 1),
            (1, 4),
        }
        assert g.adjacent(1) == {2, 4} and g.is_adjacent(1, 2) and g.is_adjacent(1, 4)
        assert g.adjacent(2) == {3, 1} and g.is_adjacent(2, 3) and g.is_adjacent(1, 2)
        assert g.adjacent(3) == {2, 4} and g.is_adjacent(3, 2) and g.is_adjacent(3, 4)
        assert g.adjacent(4) == {1, 3} and g.is_adjacent(1, 4) and g.is_adjacent(3, 4)
        g.remove_nodes(1, 2)
        assert g.nodes() == {3, 4}
        assert g.edges() == {(3, 4), (4, 3)}
        assert g.adjacent(3) == {4} and g.is_adjacent(4, 3)
        assert g.adjacent(4) == {3} and g.is_adjacent(4, 3)
        g.remove((3, 4))
        assert g.nodes() == {3, 4}
        assert g.edges() == set()
        assert g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(3, 4)

    def test_directed_graph(self):
        g = Graph[int](directed=True)
        g.remove_nodes(1)  # delete non-existent node
        g.add_nodes(1, 2, 3, 4)
        assert g.adjacent(1) == g.adjacent(2) == g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(1, 2)
        g.add((1, 2), (2, 3), (3, 4), (4, 1))
        assert g.edges() == {(1, 2), (2, 3), (3, 4), (4, 1)}
        assert g.adjacent(1) == {2} and g.is_adjacent(1, 2) and not g.is_adjacent(2, 1)
        assert g.adjacent(2) == {3} and g.is_adjacent(2, 3) and not g.is_adjacent(3, 2)
        assert g.adjacent(3) == {4} and g.is_adjacent(3, 4) and not g.is_adjacent(4, 3)
        assert g.adjacent(4) == {1} and g.is_adjacent(4, 1) and not g.is_adjacent(1, 4)
        g.remove_nodes(1, 2)
        assert g.nodes() == {3, 4}
        assert g.edges() == {(3, 4)}
        assert g.adjacent(3) == {4} and g.is_adjacent(3, 4)
        assert g.adjacent(4) == set() and not g.is_adjacent(4, 3)
        g.remove((4, 3))  # delete non-existent edge
        assert g.nodes() == {3, 4}
        assert g.edges() == {(3, 4)}
        assert g.adjacent(3) == {4} and g.is_adjacent(3, 4)
        g.remove((3, 4))
        assert g.nodes() == {3, 4}
        assert g.edges() == set()
        assert g.adjacent(3) == g.adjacent(4) == set()
        assert not g.is_adjacent(3, 4)


class TestComponents:
    def test_when_vertex_does_not_exist_then_return_empty_collection(self):
        g = Graph[int](directed=False)
        g.add((1, 2))
        assert g.connected_component(99) == set()
        g = Graph[int](directed=True)
        g.add_nodes((1, 2))
        assert g.connected_component(99) == set()

    def test_a_vertex_with_no_incident_edges_is_itself_a_component(self):
        g = Graph[int](directed=False)
        g.add_nodes(1)
        assert g.connected_component(1) == {1}
        g = Graph[int](directed=True)
        g.add_nodes(1)
        assert g.connected_component(1) == {1}

    def test_a_connected_graph_has_exactly_one_component(self):
        g = Graph[int](directed=False)
        g.add((1, 2), (2, 3))
        assert g.connected_component(1) == g.nodes()
        assert g.connected_component(2) == g.nodes()
        assert g.connected_component(3) == g.nodes()
        g = Graph[int](directed=True)
        g.add((1, 2), (2, 3), (3, 1))
        assert g.connected_component(1) == g.nodes()
        assert g.connected_component(2) == g.nodes()
        assert g.connected_component(3) == g.nodes()

    @pytest.mark.skip
    def test_directed_graph(self):
        g = Graph[int](directed=True)
        g.add((1, 2), (2, 3))
        assert g.connected_component(1) == {1}
        assert g.connected_component(2) == {2}
        assert g.connected_component(3) == {3}


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
