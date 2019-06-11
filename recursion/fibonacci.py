"""
Generate the nth Fibonacci number.
The fibonacci sequence starts from 0, like the following: 0, 1, 1, 2, 3, 5, 8, ...
"""


def fib(n):
    """There are 2 branches per call, and we go as deep as `n`, therefore the runtime is 0 (2^n)."""
    if n < 1:
        raise ValueError('n must not be less than 1')
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
