
def fib(n):
    # Generate the nth Fibonacci number.
    # The fibonacci sequence starts from 0, like the following: 0, 1, 1, 2, 3, 5, 8, ...
    if n < 1:
        raise ValueError('n must not be less than 1')
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
