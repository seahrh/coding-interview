"""
Generate the nth Fibonacci number.
The fibonacci sequence starts from 0, like the following:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Recurrence relation: F(n) = F(n-1) + F(n-2)
"""
from typing import List


def fib_rec(n: int) -> int:
    """There are 2 branches per call, and we go as deep as N, therefore exponential time (2^N).
    O(n) space: recursive call stack.
    """
    if n < 1:
        raise ValueError("n must not be less than 1")
    # base cases fib(1) and fib(2)
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_memo(n: int) -> int:
    if n < 1:
        raise ValueError("n must not be less than 1")
    # base cases fib(1) and fib(2)
    _unknown = -1
    _memo = [_unknown] * max(n, 2)
    _memo[0] = 0
    _memo[1] = 1

    def _fib(nth: int, memo: List[int], unknown: int) -> int:
        if memo[nth - 1] != unknown:
            return memo[nth - 1]
        memo[nth - 1] = _fib(nth - 1, memo, unknown) + _fib(nth - 2, memo, unknown)
        return memo[nth - 1]

    return _fib(n, _memo, _unknown)
