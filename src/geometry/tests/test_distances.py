from geometry.distances import *


class TestEuclideanDistance:
    def test_euclidean_distance(self):
        assert euclidean_distance([1], [1]) == 0
        assert euclidean_distance([1], [0]) == 1
        assert euclidean_distance([0], [1]) == 1
        p = [2, -1]
        q = [-2, 2]
        assert euclidean_distance(p, q) == 5
        assert euclidean_distance(q, p) == 5
