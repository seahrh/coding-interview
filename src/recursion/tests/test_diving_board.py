import pytest
from recursion.diving_board import *


class TestDivingBoardRecursive:
    def test_when_k_is_less_than_1_then_raise_error(self):
        with pytest.raises(ValueError):
            all_lengths_rec(k=0, shorter=1, longer=2)

    def test_when_k_equals_1(self):
        assert all_lengths_rec(k=1, shorter=1, longer=2) == {1, 2}

    def test_when_k_equals_2(self):
        assert all_lengths_rec(k=2, shorter=1, longer=2) == {2, 3, 4}

    def test_when_k_equals_3(self):
        assert all_lengths_rec(k=3, shorter=1, longer=2) == {3, 4, 5, 6}

    def test_when_k_equals_4(self):
        assert all_lengths_rec(k=4, shorter=1, longer=2) == {4, 5, 6, 7, 8}


class TestDivingBoard:
    def test_when_k_is_less_than_1_then_raise_error(self):
        with pytest.raises(ValueError):
            all_lengths(k=0, shorter=1, longer=2)

    def test_when_k_equals_1(self):
        assert all_lengths(k=1, shorter=1, longer=2) == {1, 2}

    def test_when_k_equals_2(self):
        assert all_lengths(k=2, shorter=1, longer=2) == {2, 3, 4}

    def test_when_k_equals_3(self):
        assert all_lengths(k=3, shorter=1, longer=2) == {3, 4, 5, 6}

    def test_when_k_equals_4(self):
        assert all_lengths(k=4, shorter=1, longer=2) == {4, 5, 6, 7, 8}
