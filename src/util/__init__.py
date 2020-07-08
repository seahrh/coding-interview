from typing import Iterable, TypeVar, List, Union


T = TypeVar("T")
Numeric = Union[int, float]


def argmin(elements: Iterable[T]) -> int:
    """Returns first index of smallest element."""
    return min(enumerate(elements), key=lambda x: x[1])[0]


def argmax(elements: Iterable[T]) -> int:
    """Returns first index of largest element."""
    return max(enumerate(elements), key=lambda x: x[1])[0]


def dot(p: List[List[Numeric]], q: List[List[Numeric]]) -> List[List[float]]:
    """Matrix dot product."""
    p_shape = len(p), len(p[0])
    q_shape = len(q), len(q[0])
    if p_shape[1] != q_shape[0]:
        raise ValueError("number of columns in p must equal the number of rows in q")
    res: List[List[float]] = [[0.0] * q_shape[1] for _ in range(p_shape[0])]
    for i in range(p_shape[0]):
        for j in range(q_shape[1]):
            for k in range(p_shape[1]):
                res[i][j] += p[i][k] * q[k][j]
    return res
