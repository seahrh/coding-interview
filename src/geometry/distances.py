import math
from typing import List


def euclidean_distance(p: List[float], q: List[float]) -> float:
    """The Euclidean distance or Euclidean metric is the "ordinary" straight-line distance
    between two points in Euclidean space. With this distance, Euclidean space becomes a metric space.
    The associated norm is called the Euclidean norm.
    A generalized term for the Euclidean norm is the L2 norm or L2 distance.
    """
    if p is None or len(p) == 0:
        raise ValueError("p must not be None or empty")
    if q is None or len(q) == 0:
        raise ValueError("q must not be None or empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same dimension")
    res: float = 0
    for i in range(len(p)):
        res += (q[i] - p[i]) ** 2
    res = math.sqrt(res)
    return res
