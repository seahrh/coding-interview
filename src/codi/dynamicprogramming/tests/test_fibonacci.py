from codi.dynamicprogramming.fibonacci import *


class TestFibonacciRecursive:
    def test_fib(self):
        assert fib_rec(1) == 0
        assert fib_rec(2) == 1
        assert fib_rec(7) == 8
        assert fib_rec(9) == 21


class TestFibonacciMemoization:
    def test_fib(self):
        assert fib_memo(1) == 0
        assert fib_memo(2) == 1
        assert fib_memo(7) == 8
        assert fib_memo(9) == 21


class TestFibonacci:
    def test_fib(self):
        assert fib(1) == 0
        assert fib(2) == 1
        assert fib(7) == 8
        assert fib(9) == 21
