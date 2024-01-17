import math
from typing import Iterable, List, Union

Numeric = Union[int, float]


def magnitude(p: Iterable[Numeric]) -> float:
    res: float = 0
    for component in p:
        res += component**2
    res = math.sqrt(res)
    return res


def vdot(p: List[Numeric], q: List[Numeric]) -> float:
    """Vector dot product."""
    if len(p) == 0:
        raise ValueError("p must not be None or empty")
    if len(q) == 0:
        raise ValueError("q must not be None or empty")
    if len(p) != len(q):
        raise ValueError("vectors p and q must have the same dimension")
    res: float = 0
    for i in range(len(p)):
        res += p[i] * q[i]
    return res


def full(rows: int, columns: int, fill: Numeric = 0) -> List[List[float]]:
    """Return a new array of given shape and type, filled with fill_value."""
    return [[fill] * columns for _ in range(rows)]


def transpose(mat: List[List[Numeric]]) -> List[List[float]]:
    res: List[List[float]] = full(rows=len(mat[0]), columns=len(mat))
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            res[i][j] = mat[j][i]
    return res


def dot(p: List[List[Numeric]], q: List[List[Numeric]]) -> List[List[float]]:
    """Matrix dot product."""
    p_shape = len(p), len(p[0])
    q_shape = len(q), len(q[0])
    if p_shape[1] != q_shape[0]:
        raise ValueError("number of columns in p must equal the number of rows in q")
    res: List[List[float]] = full(rows=p_shape[0], columns=q_shape[1])
    for i in range(p_shape[0]):
        for j in range(q_shape[1]):
            for k in range(p_shape[1]):
                res[i][j] += p[i][k] * q[k][j]
    return res
