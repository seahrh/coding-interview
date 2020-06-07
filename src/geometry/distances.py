import math
from typing import List, Iterable


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


def magnitude(p: Iterable[float]) -> float:
    res: float = 0
    for component in p:
        res += component ** 2
    res = math.sqrt(res)
    return res


def dot_product(p: List[float], q: List[float]) -> float:
    if p is None or len(p) == 0:
        raise ValueError("p must not be None or empty")
    if q is None or len(q) == 0:
        raise ValueError("q must not be None or empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same dimension")
    res: float = 0
    for i in range(len(p)):
        res += p[i] * q[i]
    return res


def cosine_similarity(p: List[float], q: List[float]) -> float:
    """Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space.
    It is defined to equal the cosine of the angle between them,
    which is also the same as the inner product of the same vectors normalized to both have length 1.
    The resulting similarity ranges from −1 meaning exactly opposite, to 1 meaning exactly the same,
    with 0 indicating orthogonality or decorrelation,
    while in-between values indicate intermediate similarity or dissimilarity.
    """
    if p is None or len(p) == 0:
        raise ValueError("p must not be None or empty")
    if q is None or len(q) == 0:
        raise ValueError("q must not be None or empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same dimension")
    return dot_product(p, q) / (magnitude(p) * magnitude(q))
