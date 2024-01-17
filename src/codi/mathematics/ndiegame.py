import math


def price(n: int) -> float:
    """Price of the die game equals the expected return of the N-die game."""
    if n == 1:
        return (1 + 2 + 3 + 4 + 5 + 6) / 6
    less = price(n - 1)
    # p is the probability of rolling the n-th dice
    p = int(less) / 6
    res = less * (1 - p)
    lo = math.ceil(less)
    denom = 6 - lo + 1
    for i in range(lo, 7):
        res += p * i / denom
    return res
