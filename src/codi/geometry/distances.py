import math
from typing import List, TypeVar

from codi.geometry.linear_algebra import magnitude, vdot

T = TypeVar("T")


def cosine_similarity(p: List[float], q: List[float]) -> float:
    """Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space.
    It is defined to equal the cosine of the angle between them,
    which is also the same as the inner product of the same vectors normalized to both have length 1.
    The resulting similarity ranges from −1 meaning exactly opposite, to 1 meaning exactly the same,
    with 0 indicating orthogonality or decorrelation,
    while in-between values indicate intermediate similarity or dissimilarity.
    """
    if len(p) == 0:
        raise ValueError("p must not be None or empty")
    if len(q) == 0:
        raise ValueError("q must not be None or empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same dimension")
    return vdot(p, q) / (magnitude(p) * magnitude(q))


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
        _sum += abs(q[i] - p[i])
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
        _sum += abs(q[i] - p[i]) / max_diff
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


def jaccard_distance(p: List[bool], q: List[bool]) -> float:
    """Jaccard distance is intended for boolean variables (e.g. norminal variables after one-hot encoding).

    Based on https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html
    """
    if len(p) == 0:
        raise ValueError("p must not be empty")
    if len(q) == 0:
        raise ValueError("q must not be empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same number of components")
    tt = 0
    ne = 0
    for i in range(len(p)):
        if p[i] and q[i]:  # both True
            tt += 1
        elif p[i] != q[i]:
            ne += 1
    union = ne + tt
    if union == 0:
        raise ValueError("p and q must not be empty")
    return float(ne / union)


def jaccard_similarity(p: List[bool], q: List[bool]) -> float:
    """Jaccard similarity or Jaccard coefficient."""
    return 1 - jaccard_distance(p, q)


def dice_distance(p: List[bool], q: List[bool]) -> float:
    """Dice distance is intended for boolean variables (e.g. norminal variables after one-hot encoding).

    Based on https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html
    """
    if len(p) == 0:
        raise ValueError("p must not be empty")
    if len(q) == 0:
        raise ValueError("q must not be empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same number of components")
    tt = 0
    ne = 0
    for i in range(len(p)):
        if p[i] and q[i]:  # both True
            tt += 1
        elif p[i] != q[i]:
            ne += 1
    total_size = 2 * tt + ne  # combined size of p and q sets
    if total_size == 0:
        raise ValueError("p and q must not be empty")
    return float(ne / total_size)


def dice_similarity(p: List[bool], q: List[bool]) -> float:
    """Dice similarity or Dice coefficient."""
    return 1 - dice_distance(p, q)
