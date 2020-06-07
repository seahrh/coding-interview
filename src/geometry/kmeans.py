import random
import sys
from typing import List, Callable
from geometry.distances import euclidean_distance


def centroid(cluster: List[List[float]]) -> List[float]:
    if cluster is None or len(cluster) == 0:
        raise ValueError("cluster must not be None or empty")
    res: List[float] = [0] * len(cluster[0])
    for member in cluster:
        for i in range(len(member)):
            res[i] += member[i] / len(cluster)
    return res


def naive_kmeans(
    data: List[List[float]],
    k: int,
    iterations: int,
    distance: Callable = euclidean_distance,
) -> List[List[List[float]]]:
    """Naive K-means algorithm:

    1. Assignment step: Assign each observation to the cluster with the nearest mean
    (i.e. that with the least squared Euclidean distance).

    2. Update step: Recalculate means (centroids) for observations assigned to each cluster.

    :param data: list of vectors
    :param k: number of clusters
    :param iterations: number of iterations
    :param distance: distance function, Euclidean distance (L2 norm) by default
    :return: List of clusters, where each cluster is a list of vectors.
    """
    if len(data) < k:
        raise ValueError("Number of data points must be at least k")
    # random sampling without replacement
    centroids: List[List[float]] = random.sample(data, k)
    # centroid is the prototype; it should not appear in the clusters.
    res: List[List[List[float]]] = []
    for _ in range(iterations):
        res = [[] for _ in range(k)]
        # assignment step
        for v in data:
            _min = sys.maxsize
            _min_index = -1
            for i, c in enumerate(centroids):
                d = distance(v, c)
                if d < _min:
                    _min = d
                    _min_index = i
            res[_min_index].append(v)
        # update step
        centroids = []
        for cluster in res:
            centroids.append(centroid(cluster))
    return res
