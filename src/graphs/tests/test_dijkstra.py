from graphs.dijkstra import *
from graphs.graph import Edge


class TestDijkstraShortestPath:
    _MAX_COST: int = 999

    def test_graph_of_three_nodes_or_less(self):
        g = DiGraph[int]()
        g.add_nodes(1)
        assert distances(g, source=1, max_cost=self._MAX_COST) == {
            1: Distance(0, child=1, parent=None)
        }
        g.add_nodes(2)
        assert distances(g, source=1, max_cost=self._MAX_COST) == {
            1: Distance(0, child=1, parent=None),
            2: Distance(self._MAX_COST, child=2, parent=None),
        }
        assert distances(g, source=2, max_cost=self._MAX_COST) == {
            1: Distance(self._MAX_COST, child=1, parent=None),
            2: Distance(0, child=2, parent=None),
        }
        g.add(Edge(1, 2, weight=10), Edge(1, 3, weight=1), Edge(3, 2, weight=2))
        assert distances(g, source=1) == {
            1: Distance(0, child=1, parent=None),
            2: Distance(3, child=2, parent=3),
            3: Distance(1, child=3, parent=1),
        }
        assert distances(g, source=2, max_cost=self._MAX_COST) == {
            1: Distance(self._MAX_COST, child=1, parent=None),
            2: Distance(0, child=2, parent=None),
            3: Distance(self._MAX_COST, child=3, parent=None),
        }
        assert distances(g, source=3, max_cost=self._MAX_COST) == {
            1: Distance(self._MAX_COST, child=1, parent=None),
            2: Distance(2, child=2, parent=3),
            3: Distance(0, child=3, parent=None),
        }

    def test_case_1(self):
        g = DiGraph[int]()
        g.add(
            Edge(1, 2, weight=50),
            Edge(2, 3, weight=10),
            Edge(1, 3, weight=45),
            Edge(1, 4, weight=10),
            Edge(4, 1, weight=10),
            Edge(2, 4, weight=15),
            Edge(4, 5, weight=15),
            Edge(5, 2, weight=20),
            Edge(5, 3, weight=35),
            Edge(3, 5, weight=30),
            Edge(6, 5, weight=3),
        )
        assert distances(g, source=1, max_cost=self._MAX_COST) == {
            1: Distance(cost=0, child=1, parent=None),
            2: Distance(cost=45, child=2, parent=5),
            3: Distance(cost=45, child=3, parent=1),
            4: Distance(cost=10, child=4, parent=1),
            5: Distance(cost=25, child=5, parent=4),
            6: Distance(cost=self._MAX_COST, child=6, parent=None),
        }
        assert distances(g, source=2, max_cost=self._MAX_COST) == {
            1: Distance(cost=25, child=1, parent=4),
            2: Distance(cost=0, child=2, parent=None),
            3: Distance(cost=10, child=3, parent=2),
            4: Distance(cost=15, child=4, parent=2),
            5: Distance(cost=30, child=5, parent=4),
            6: Distance(cost=self._MAX_COST, child=6, parent=None),
        }
        assert distances(g, source=3, max_cost=self._MAX_COST) == {
            1: Distance(cost=75, child=1, parent=4),
            2: Distance(cost=50, child=2, parent=5),
            3: Distance(cost=0, child=3, parent=None),
            4: Distance(cost=65, child=4, parent=2),
            5: Distance(cost=30, child=5, parent=3),
            6: Distance(cost=self._MAX_COST, child=6, parent=None),
        }
        assert distances(g, source=4, max_cost=self._MAX_COST) == {
            1: Distance(cost=10, child=1, parent=4),
            2: Distance(cost=35, child=2, parent=5),
            3: Distance(cost=45, child=3, parent=2),
            4: Distance(cost=0, child=4, parent=None),
            5: Distance(cost=15, child=5, parent=4),
            6: Distance(cost=self._MAX_COST, child=6, parent=None),
        }
        assert distances(g, source=5, max_cost=self._MAX_COST) == {
            1: Distance(cost=45, child=1, parent=4),
            2: Distance(cost=20, child=2, parent=5),
            3: Distance(cost=30, child=3, parent=2),
            4: Distance(cost=35, child=4, parent=2),
            5: Distance(cost=0, child=5, parent=None),
            6: Distance(cost=self._MAX_COST, child=6, parent=None),
        }
        assert distances(g, source=6, max_cost=self._MAX_COST) == {
            1: Distance(cost=48, child=1, parent=4),
            2: Distance(cost=23, child=2, parent=5),
            3: Distance(cost=33, child=3, parent=2),
            4: Distance(cost=38, child=4, parent=2),
            5: Distance(cost=3, child=5, parent=6),
            6: Distance(cost=0, child=6, parent=None),
        }
