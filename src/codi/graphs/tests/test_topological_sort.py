from codi.graphs.topological_sort import *


class TestFindCycle:
    def test_two_edges_or_less(self):
        g = DiGraph[int]()
        g.add_nodes(1)
        assert not has_cycle(g)
        g.add_nodes(1, 2)
        assert not has_cycle(g)
        g.add(Edge(1, 2))
        assert not has_cycle(g)
        g.add(Edge(2, 1))
        assert find_cycle(g).edges() == {Edge(1, 2), Edge(2, 1)}

    def test_edge_between_parent_and_grandchild(self):
        g = DiGraph[int]()
        g.add(Edge(1, 2), Edge(2, 3), Edge(1, 3), Edge(4, 1), Edge(4, 5), Edge(5, 6))
        assert not has_cycle(g)
        g.add(Edge(6, 4))
        assert find_cycle(g).edges() == {Edge(4, 5), Edge(5, 6), Edge(6, 4)}

    def test_case_1(self):
        g = DiGraph[int]()
        g.add(Edge(4, 1), Edge(4, 2), Edge(1, 2), Edge(2, 3))
        assert not has_cycle(g)
        g.add(Edge(2, 4))
        assert find_cycle(g).edges() == {Edge(1, 2), Edge(4, 1), Edge(2, 4)}

    def test_case_2(self):
        g = DiGraph[int]()
        g.add(
            Edge(1, 3),
            Edge(2, 3),
            Edge(3, 5),
            Edge(3, 4),
            Edge(5, 6),
            Edge(5, 7),
            Edge(4, 7),
            Edge(7, 8),
        )
        assert not has_cycle(g)
        g.add(Edge(8, 1))
        assert find_cycle(g).edges() == {
            Edge(1, 3),
            Edge(8, 1),
            Edge(5, 7),
            Edge(7, 8),
            Edge(3, 5),
        }


class TestTopologicalSort:
    def test_two_edges_or_less(self):
        g = DiGraph[int]()
        g.add_nodes(1)
        assert topsort(g) == [1]
        g.add_nodes(1, 2)
        assert set(topsort(g)) == {1, 2}
        g.add(Edge(1, 2))
        assert topsort(g) == [1, 2]
        g.add(Edge(2, 1))
        assert topsort(g) == []  # has cycle

    def test_edge_between_parent_and_grandchild(self):
        g = DiGraph[int]()
        g.add(Edge(1, 2), Edge(2, 3), Edge(1, 3), Edge(4, 1), Edge(4, 5), Edge(5, 6))
        assert topsort(g) == [4, 5, 6, 1, 2, 3]
        g.add(Edge(6, 4))
        assert topsort(g) == []  # has cycle

    def test_case_1(self):
        g = DiGraph[int]()
        g.add(Edge(4, 1), Edge(4, 2), Edge(1, 2), Edge(2, 3))
        assert topsort(g) == [4, 1, 2, 3]
        g.add(Edge(2, 4))
        assert topsort(g) == []  # has cycle

    def test_case_2(self):
        g = DiGraph[int]()
        g.add(
            Edge(1, 3),
            Edge(2, 3),
            Edge(3, 5),
            Edge(3, 4),
            Edge(5, 6),
            Edge(5, 7),
            Edge(4, 7),
            Edge(7, 8),
        )
        a = topsort(g)
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
        g.add(Edge(8, 1))
        assert topsort(g) == []  # has cycle
