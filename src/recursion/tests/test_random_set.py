import pytest
from recursion.random_set import *


class TestRandomSetRecursive:
    def test_given_array_too_small_to_fill_set(self):
        with pytest.raises(ValueError):
            pick_rec(arr=[1], m=2, index=0)

    def test_given_array_of_length_one_and_m_equals_one(self):
        assert pick_rec(arr=[0], m=1, index=0) == [0]

    def test_given_array_of_length_two_and_m_is_smaller(self):
        chosen = set()
        for _ in range(40):
            for v in pick_rec(arr=[0, 1], m=1, index=1):
                chosen.add(v)
        assert 0 in chosen and 1 in chosen

    def test_given_array_of_length_10_and_m_is_smaller(self):
        chosen = set()
        for _ in range(40):
            for v in pick_rec(arr=list(range(10)), m=5, index=9):
                chosen.add(v)
        for i in range(10):
            assert i in chosen


class TestRandomSet:
    def test_given_array_too_small_to_fill_set(self):
        with pytest.raises(ValueError):
            pick(arr=[1], m=2)

    def test_given_array_of_length_one_and_m_equals_one(self):
        assert pick(arr=[0], m=1) == [0]

    def test_given_array_of_length_two_and_m_is_smaller(self):
        chosen = set()
        for _ in range(40):
            for v in pick(arr=[0, 1], m=1):
                chosen.add(v)
        assert 0 in chosen and 1 in chosen

    def test_given_array_of_length_10_and_m_is_smaller(self):
        chosen = set()
        for _ in range(40):
            for v in pick(arr=list(range(10)), m=5):
                chosen.add(v)
        for i in range(10):
            assert i in chosen
