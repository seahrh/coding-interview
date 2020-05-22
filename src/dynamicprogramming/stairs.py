"""
Number of ways to climb stairs:
If a person can climb either 1 stair or 2 stairs at a time, for a given n stairs, how many ways a
person can reach the top from bottom?
Optional:
What if a person can climb any number from a set X, for example if X = {1,2,4}, then he/she
can climb 1, 2 or 4 stairs at a time. How many ways he/she can climb from bottom to top?
"""
from typing import Set, List


def climb_rec(n: int, steps: Set[int]) -> int:
    """
    N is the total number of steps in stairs, M is the number of steps allowed in one move.
    Time O(NM): recursive call stack goes down one branch only; at each level consider M steps.
    Space O(N): size of cache, recursive call stack
    """
    if n < 1:
        raise ValueError("n must not be less than 1")
    unknown = 0
    memo: List[int] = [unknown] * (n + 1)
    # bring remaining steps to zero, counts as 1 valid move.
    memo[0] = 1

    def _climb(_n: int) -> int:
        # base case: overshoots the remaining steps required, not counted as a valid move.
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


def climb(n: int, steps: Set[int]) -> int:
    """Replace recursion with iteration (time and space complexity unchanged).
    N is the total number of steps in stairs, M is the number of steps in one move.
    Time O(NM)
    Space O(N): size of cache
    """
    if n < 1:
        raise ValueError("n must not be less than 1")
    unknown = 0
    memo: List[int] = [unknown] * (n + 1)
    # bring remaining steps to zero, counts as 1 valid move.
    memo[0] = 1

    for i in range(1, n + 1):  # fill the memo array from left to right
        _sum = 0
        for s in steps:
            remaining = i - s
            if remaining >= 0:
                _sum += memo[remaining]
        memo[i] = _sum

    return memo[n]
