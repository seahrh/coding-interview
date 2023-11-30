import pytest

from datastructures.calculator import *


class TestCalculator:
    def test_given_expression_too_short_then_raise_error(self):
        with pytest.raises(ValueError):
            calculate("2 *         ")

    def test_given_example_1(self):
        assert calculate("2 * 3 + 5 / 6 * 3 + 15") == 23.5

    def test_given_example_2(self):
        assert calculate("2 - 6 - 7 * 8 / 2 + 5") == -27

    def test_given_low_priority_operator_in_the_middle_of_high_priority_operators(self):
        assert calculate("10 - 7 * 8 + 4 / 2 + 5") == -39
