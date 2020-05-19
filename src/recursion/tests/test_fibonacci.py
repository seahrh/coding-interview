from recursion.fibonacci import *


class TestFibonacci:
    def test_fib_numbers(self):
        assert fib(1) == 0
        assert fib(2) == 1
        assert fib(7) == 8
