from geometry.distances import *


class TestManhattanDistance:
    def test_manhattan_distance(self):
        assert manhattan_distance([1], [1]) == 0
        assert manhattan_distance([1], [0]) == 1
        assert manhattan_distance([0], [1]) == 1
        p = [2, -1]
        q = [-2, 2]
        assert manhattan_distance(p, q) == 7
        assert manhattan_distance(q, p) == 7


class TestManhattanSimilarity:
    def test_manhattan_similarity(self):
        max_diff = 10
        assert manhattan_similarity([1], [1], max_diff) == 1
        assert manhattan_similarity([1], [0], max_diff) == 0.9
        assert manhattan_similarity([0], [1], max_diff) == 0.9
        p = [2, -1]
        q = [-2, 2]
        assert manhattan_similarity(p, q, max_diff) == 0.65
        assert manhattan_similarity(q, p, max_diff) == 0.65
        p = [1, 2, 3, 4]
        q = [4, 3, 2, 1]
        assert manhattan_similarity(p, q, max_diff) == 0.8
        assert manhattan_similarity(q, p, max_diff) == 0.8
        p = [1, 0, 1, 0, 1]
        q = [1, 1, 0, 0, 1]
        assert manhattan_similarity(p, q, max_diff=1) == 0.6
        assert manhattan_similarity(q, p, max_diff=1) == 0.6


class TestEuclideanDistance:
    def test_euclidean_distance(self):
        assert euclidean_distance([1], [1]) == 0
        assert euclidean_distance([1], [0]) == 1
        assert euclidean_distance([0], [1]) == 1
        p = [2, -1]
        q = [-2, 2]
        assert euclidean_distance(p, q) == 5
        assert euclidean_distance(q, p) == 5


class TestCosineSimilarity:
    def test_cosine_similarity(self):
        assert cosine_similarity([1], [1]) == 1
        assert cosine_similarity([1], [-1]) == -1
        assert cosine_similarity([-1], [1]) == -1
        p = [1, -1, 1, 1]
        q = [1, 1, 1, 1]
        assert cosine_similarity(p, q) == 0.5
        assert cosine_similarity(q, p) == 0.5


class TestHammingDistance:
    def test_hamming_distance(self):
        assert hamming_distance([1], [1]) == 0
        assert hamming_distance([1], [0]) == 1
        assert hamming_distance([0], [1]) == 1
        p = [2, -1]
        q = [-2, 2]
        assert hamming_distance(p, q) == 2
        assert hamming_distance(q, p) == 2
        assert hamming_distance(list("karolin"), list("karolin")) == 0
        assert hamming_distance(list("karolin"), list("kathrin")) == 3
        assert hamming_distance(list("karolin"), list("kerstin")) == 3
        assert hamming_distance(list("1011101"), list("1001001")) == 2


class TestJaccardDistance:
    def test_2_or_less_components(self):
        assert jaccard_distance([False], [True]) == 1
        assert jaccard_distance([True], [False]) == 1
        assert jaccard_distance([True], [True]) == 0
        assert jaccard_distance([False, False], [False, True]) == 1
        assert jaccard_distance([False, False], [True, False]) == 1
        assert jaccard_distance([False, False], [True, True]) == 1
        assert jaccard_distance([False, True], [False, False]) == 1
        assert jaccard_distance([False, True], [False, True]) == 0
        assert jaccard_distance([False, True], [True, False]) == 1
        assert jaccard_distance([False, True], [True, True]) == 0.5
        assert jaccard_distance([True, False], [False, False]) == 1
        assert jaccard_distance([True, False], [False, True]) == 1
        assert jaccard_distance([True, False], [True, False]) == 0
        assert jaccard_distance([True, False], [True, True]) == 0.5
        assert jaccard_distance([True, True], [False, False]) == 1
        assert jaccard_distance([True, True], [False, True]) == 0.5
        assert jaccard_distance([True, True], [True, False]) == 0.5
        assert jaccard_distance([True, True], [True, True]) == 0


class TestDiceDistance:
    def test_2_or_less_components(self):
        assert dice_distance([False], [True]) == 1
        assert dice_distance([True], [False]) == 1
        assert dice_distance([True], [True]) == 0
        assert dice_distance([False, False], [False, True]) == 1
        assert dice_distance([False, False], [True, False]) == 1
        assert dice_distance([False, False], [True, True]) == 1
        assert dice_distance([False, True], [False, False]) == 1
        assert dice_distance([False, True], [False, True]) == 0
        assert dice_distance([False, True], [True, False]) == 1
        assert dice_distance([False, True], [True, True]) == 1 / 3
        assert dice_distance([True, False], [False, False]) == 1
        assert dice_distance([True, False], [False, True]) == 1
        assert dice_distance([True, False], [True, False]) == 0
        assert dice_distance([True, False], [True, True]) == 1 / 3
        assert dice_distance([True, True], [False, False]) == 1
        assert dice_distance([True, True], [False, True]) == 1 / 3
        assert dice_distance([True, True], [True, False]) == 1 / 3
        assert dice_distance([True, True], [True, True]) == 0
