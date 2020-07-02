from graphs.graph import Edge
from graphs.dijkstra import *


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
