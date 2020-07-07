import math
from typing import List, Iterable, TypeVar


T = TypeVar("T")


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


def hamming_distance(p: List[T], q: List[T]) -> int:
    """In information theory, the Hamming distance between two strings of equal length is the number of positions
    at which the corresponding symbols are different. In other words, it measures the minimum number of
    substitutions required to change one string into the other,
    or the minimum number of errors that could have transformed one string into the other.
    """
    if len(p) == 0:
        raise ValueError("p must not be empty")
    if len(q) == 0:
        raise ValueError("q must not be empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same number of components")
    res: int = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            res += 1
    return res


def manhattan_distance(p: List[float], q: List[float]) -> float:
    """Sum of absolute differences.
     The taxicab metric is also known as rectilinear distance, L1 norm. L1 distance or Manhattan distance.
    """
    if len(p) == 0:
        raise ValueError("p must not be empty")
    if len(q) == 0:
        raise ValueError("q must not be empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same number of components")
    _sum: float = 0
    for i in range(len(p)):
        _sum += math.fabs(q[i] - p[i])
    return _sum


def manhattan_similarity(p: List[float], q: List[float], max_diff: float) -> float:
    """Manhattan similarity measure in the range [0, 1] where 1 means perfect similarity.
    The absolute differences are range normalized, then take the average of the differences.

    :param p: Vector p
    :param q: Vector q
    :param max_diff: largest possible difference (smallest difference is of course zero)
    :return:
    """
    if len(p) == 0:
        raise ValueError("p must not be empty")
    if len(q) == 0:
        raise ValueError("q must not be empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same number of components")
    _sum: float = 0
    for i in range(len(p)):
        _sum += math.fabs(q[i] - p[i]) / max_diff
    return 1 - _sum / len(p)


def euclidean_distance(p: List[float], q: List[float]) -> float:
    """Square root of the sum of squared differences.
    The Euclidean distance or Euclidean metric is the "ordinary" straight-line distance
    between two points in Euclidean space. With this distance, Euclidean space becomes a metric space.
    The associated norm is called the Euclidean norm, L2 norm or L2 distance.
    """
    if len(p) == 0:
        raise ValueError("p must not be empty")
    if len(q) == 0:
        raise ValueError("q must not be empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same number of components")
    _sum: float = 0
    for i in range(len(p)):
        _sum += (q[i] - p[i]) ** 2
    return math.sqrt(_sum)
