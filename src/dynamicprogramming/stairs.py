"""
Number of ways to climb stairs:
If a person can climb either 1 stair or 2 stairs at a time, for a given n stairs, how many ways a
person can reach the top from bottom?
Optional:
What if a person can climb any number from a set X, for example if X = {1,2,4}, then he/she
can climb 1, 2 or 4 stairs at a time. How many ways he/she can climb from bottom to top?
"""
from typing import Set, List


def climb(n: int, steps: Set[int]) -> int:
    if n < 1:
        raise ValueError("n must not be less than 1")
    unknown = 0
    memo: List[int] = [unknown] * (n + 1)
    memo[0] = 1

    def _climb(_n: int) -> int:
        if _n < 0:
            return 0
        if memo[_n] != unknown:
            return memo[_n]
        res = 0
        for s in steps:
            memo[_n - s] = _climb(_n - s)
            res += memo[_n - s]
        return res

    return _climb(n)
