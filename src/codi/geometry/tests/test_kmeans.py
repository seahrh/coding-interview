from codi.geometry.kmeans import *


class TestCentroid:
    def test_centroid(self):
        assert centroid([[1, 1], [1, 1]]) == [1, 1]
        assert centroid([[1, 1], [-1, -1]]) == [0, 0]
        assert centroid([[-5, 1], [-1, -9], [9, 2], [-7, 14]]) == [-1, 2]


class TestNaiveKMeans:
    def test_naive_kmeans(self):
        assert naive_kmeans([[1, 1]], k=1, iterations=4) == [[[1, 1]]]
        assert sorted(naive_kmeans([[1, 1], [9, 9]], k=2, iterations=4)) == [
            [[1, 1]],
            [[9, 9]],
        ]
        assert sorted(
            naive_kmeans(
                [
                    [1, 1],
                    [-90, -91],
                    [1.1, 0.9],
                    [1.2, 0.8],
                    [-90.1, -80.9],
                    [-90.2, -80.8],
                ],
                k=2,
                iterations=4,
            )
        ) == [
            [[-90, -91], [-90.1, -80.9], [-90.2, -80.8]],
            [[1, 1], [1.1, 0.9], [1.2, 0.8]],
        ]
