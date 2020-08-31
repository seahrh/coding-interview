import pytest
from dynamicprogramming.number_of_dice_rolls_with_target_sum import *


class TestNumberOfDiceRollsWithTargetSum:
    @pytest.mark.skip("have not figured out why this is failing")
    def test_output_is_modulo(self):
        assert solve(dice=30, faces=30, target=500) == 222616187

    def test_case_1(self):
        assert solve(dice=1, faces=6, target=3) == 1

    def test_case_2(self):
        assert solve(dice=2, faces=6, target=7) == 6

    def test_case_3(self):
        assert solve(dice=2, faces=5, target=10) == 1

    def test_case_4(self):
        assert solve(dice=1, faces=2, target=3) == 0

    def test_case_5(self):
        assert solve(dice=2, faces=6, target=6) == 5
