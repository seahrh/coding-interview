from graphs.graph import Edge
from graphs.dijkstra import *


class TestDijkstraShortestPath:
    def test_graph_of_three_nodes_or_less(self):
        g = DiGraph[int]()
        g.add_nodes(1)
        assert distances(g, source=1) == {1: Distance(0, child=1, parent=None)}
        g.add_nodes(2)
        assert distances(g, source=1) == {
            1: Distance(0, child=1, parent=None),
            2: Distance(sys.maxsize, child=2, parent=None),
        }
        assert distances(g, source=2) == {
            1: Distance(sys.maxsize, child=1, parent=None),
            2: Distance(0, child=2, parent=None),
        }
        g.add(Edge(left=1, right=2, weight=2), Edge(left=1, right=3, weight=3))
