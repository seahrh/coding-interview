"""
N Queens
==========
Place N queens on a NxN chessboard such that no queens come under attack.
Give all possible placements of N queens.

SOLUTION
- Backtracking to find all possible placements
- Grow the state space tree by placing a queen on one row at a time
- Bounding function: no two queens share the same row, column and diagonal.

Time O(N!)
The worst case “brute force” solution for the N-queens puzzle has an O(n^n) time complexity.
This means it will look through every position on an NxN board, N times, for N queens.
It is by far the slowest and most impractical method.
If you refactor and prevent it from checking queens occupying the same row as each other,
it will still be brute force,
but the possible board states drop from 16,777,216 to a little over 40,000 and has a time complexity of O(n!).
"""
from typing import NamedTuple, List, Tuple, Set
import math


class Position(NamedTuple):
    row: int
    col: int


def _is_safe(q1: Position, q2: Position) -> bool:
    if q1.row == q2.row:
        return False
    if q1.col == q2.col:
        return False
    if math.fabs(q1.row - q2.row) == math.fabs(q1.col - q2.col):  # in diagonal
        return False
    return True


def _queens(n: int, partial: List[Position], result: Set[Tuple[Position, ...]]) -> None:
    if len(partial) == n:  # base case: found full solution
        result.add(tuple(partial))
        return
    row = 0
    if len(partial) != 0:
        row = partial[-1].row + 1
    for col in range(n):
        is_safe = True
        proposal = Position(row, col)
        for p in partial:
            if not _is_safe(p, proposal):
                is_safe = False
                break
        if is_safe:  # placement is safe, extend the solution
            _queens(n, partial=partial + [proposal], result=result)


def queens(n: int) -> Set[Tuple[Position, ...]]:
    if n < 1:
        raise ValueError("n must not be less than 1")
    res: Set[Tuple[Position, ...]] = set()
    _queens(n, partial=[], result=res)
    return res
