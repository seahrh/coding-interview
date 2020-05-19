import pytest
from others.multiples import *


class TestMultiples:
    def test_given_k_is_less_than_one_then_raise_error(self):
        with pytest.raises(ValueError):
            kth_multiple(0)

    def test_given_k_is_1(self):
        assert kth_multiple(1) == 1

    def test_given_k_is_5(self):
        assert kth_multiple(5) == 9

    def test_given_k_is_13(self):
        assert kth_multiple(13) == 63
