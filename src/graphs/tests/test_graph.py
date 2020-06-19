from graphs.graph import *


class TestGraphs:
    def test_directed_graph(self):
        g = DiGraph[int]()
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

    def test_undirected_graph(self):
        g = Graph[int]()
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


class TestFindCycle:
    def test_two_edges_or_less(self):
        g = DiGraph[int]()
        g.add_nodes(1)
        assert not g.has_cycle()
        g.add_nodes(1, 2)
        assert not g.has_cycle()
        g.add((1, 2))
        assert not g.has_cycle()
        g.add((2, 1))
        assert g.find_cycle().edges() == {(1, 2), (2, 1)}

    def test_edge_between_parent_and_grandchild(self):
        g = DiGraph[int]()
        g.add((1, 2), (2, 3), (1, 3), (4, 1), (4, 5), (5, 6))
        assert not g.has_cycle()
        g.add((6, 4))
        assert g.find_cycle().edges() == {(4, 5), (5, 6), (6, 4)}

    def test_case_1(self):
        g = DiGraph[int]()
        g.add((4, 1), (4, 2), (1, 2), (2, 3))
        assert not g.has_cycle()
        g.add((2, 4))
        assert g.find_cycle().edges() == {(1, 2), (4, 1), (2, 4)}

    def test_case_2(self):
        g = DiGraph[int]()
        g.add((1, 3), (2, 3), (3, 5), (3, 4), (5, 6), (5, 7), (4, 7), (7, 8))
        assert not g.has_cycle()
        g.add((8, 1))
        assert g.find_cycle().edges() == {(1, 3), (8, 1), (5, 7), (7, 8), (3, 5)}


class TestTopologicalSort:
    def test_two_edges_or_less(self):
        g = DiGraph[int]()
        g.add_nodes(1)
        assert g.topsort() == [1]
        g.add_nodes(1, 2)
        assert set(g.topsort()) == {1, 2}
        g.add((1, 2))
        assert g.topsort() == [1, 2]
        g.add((2, 1))
        assert g.topsort() == []  # has cycle

    def test_edge_between_parent_and_grandchild(self):
        g = DiGraph[int]()
        g.add((1, 2), (2, 3), (1, 3), (4, 1), (4, 5), (5, 6))
        assert g.topsort() == [4, 5, 6, 1, 2, 3]
        g.add((6, 4))
        assert g.topsort() == []  # has cycle

    def test_case_1(self):
        g = DiGraph[int]()
        g.add((4, 1), (4, 2), (1, 2), (2, 3))
        assert g.topsort() == [4, 1, 2, 3]
        g.add((2, 4))
        assert g.topsort() == []  # has cycle

    def test_case_2(self):
        g = DiGraph[int]()
        g.add((1, 3), (2, 3), (3, 5), (3, 4), (5, 6), (5, 7), (4, 7), (7, 8))
        a = g.topsort()
        i1 = a.index(1)
        i2 = a.index(2)
        i3 = a.index(3)
        i4 = a.index(4)
        i5 = a.index(5)
        i6 = a.index(6)
        i7 = a.index(7)
        i8 = a.index(8)
        assert i1 < i3 and i2 < i3
        assert i3 < i4 and i3 < i5
        assert i5 < i6 and i5 < i7
        assert i4 < i7
        assert i7 < i8
        g.add((8, 1))
        assert g.topsort() == []  # has cycle


class TestConnectedComponent:
    def test_when_vertex_does_not_exist_then_return_empty_graph(self):
        g = Graph[int]()
        g.add((1, 2))
        assert g.component(99).nodes() == set()

    def test_a_vertex_with_no_incident_edges_is_itself_a_component(self):
        g = Graph[int]()
        g.add_nodes(1, 2)
        assert g.component(1).nodes() == {1}
        assert g.component(2).nodes() == {2}
        c1 = Graph[int]()
        c1.add_nodes(1)
        c2 = Graph[int]()
        c2.add_nodes(2)
        assert g.components() == {c1, c2}

    def test_a_connected_graph_has_exactly_one_component(self):
        g = Graph[int]()
        g.add((1, 2), (2, 3))
        c = g.component(1)
        assert c.edges() == {(1, 2), (2, 1), (2, 3), (3, 2)}
        assert c == g.component(2) == g.component(3)
        assert g.components() == {c}

    def test_disconnected_graph(self):
        g = Graph[int]()
        g.add((1, 2), (2, 3), (4, 5), (5, 6))
        c1 = g.component(1)
        assert c1.edges() == {(1, 2), (2, 1), (2, 3), (3, 2)}
        assert c1 == g.component(2) == g.component(3)
        c2 = g.component(4)
        assert c2.edges() == {(4, 5), (5, 4), (5, 6), (6, 5)}
        assert c2 == g.component(5) == g.component(6)
        assert g.components() == {c1, c2}


class TestBreadthFirstSearch:
    def test_bfs(self):
        g = Graph[int]()
        g.add_nodes(1)
        assert g.bfs(start_node=1) == [1]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7))
        assert g.bfs(start_node=1) == [1, 2, 3, 4, 5, 6, 7]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 8), (6, 9))
        assert g.bfs(start_node=1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestDepthFirstSearch:
    def test_dfs(self):
        g = Graph[int]()
        g.add_nodes(1)
        assert g.dfs(start_node=1) == [1]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7))
        assert g.dfs(start_node=1) == [1, 3, 7, 6, 2, 5, 4]
        g = Graph[int]()
        g.add((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 8), (6, 9))
        assert g.dfs(start_node=1) == [1, 3, 7, 6, 9, 2, 5, 8, 4]
