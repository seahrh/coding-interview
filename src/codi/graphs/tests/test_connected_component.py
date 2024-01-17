from codi.graphs.connected_component import *


class TestConnectedComponent:
    def test_when_vertex_does_not_exist_then_return_empty_graph(self):
        g = Graph[int]()
        g.add(Edge(1, 2))
        assert component(g, 99).nodes() == set()

    def test_a_vertex_with_no_incident_edges_is_itself_a_component(self):
        g = Graph[int]()
        g.add_nodes(1, 2)
        assert component(g, 1).nodes() == {1}
        assert component(g, 2).nodes() == {2}
        c1 = Graph[int]()
        c1.add_nodes(1)
        c2 = Graph[int]()
        c2.add_nodes(2)
        assert components(g) == {c1, c2}

    def test_a_connected_graph_has_exactly_one_component(self):
        g = Graph[int]()
        g.add(Edge(1, 2), Edge(2, 3))
        c = component(g, 1)
        assert c.edges() == {Edge(1, 2), Edge(2, 1), Edge(2, 3), Edge(3, 2)}
        assert c == component(g, 2) == component(g, 3)
        assert components(g) == {c}

    def test_disconnected_graph(self):
        g = Graph[int]()
        g.add(Edge(1, 2), Edge(2, 3), Edge(4, 5), Edge(5, 6))
        c1 = component(g, 1)
        assert c1.edges() == {Edge(1, 2), Edge(2, 1), Edge(2, 3), Edge(3, 2)}
        assert c1 == component(g, 2) == component(g, 3)
        c2 = component(g, 4)
        assert c2.edges() == {Edge(4, 5), Edge(5, 4), Edge(5, 6), Edge(6, 5)}
        assert c2 == component(g, 5) == component(g, 6)
        assert components(g) == {c1, c2}
