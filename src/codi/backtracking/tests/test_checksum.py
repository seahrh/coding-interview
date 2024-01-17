from codi.backtracking.checksum import *


class TestChecksum:
    _IMPOSSIBLE = "IMPOSSIBLE"

    def test_2_columns_or_less(self):
        assert recover_matrix(upper_sum=1, lower_sum=1, column_sum=[2]) == "1,1"
        assert (
            recover_matrix(upper_sum=1, lower_sum=1, column_sum=[1]) == self._IMPOSSIBLE
        )
        assert recover_matrix(upper_sum=1, lower_sum=1, column_sum=[1, 1]) == "01,10"
        assert (
            recover_matrix(upper_sum=0, lower_sum=1, column_sum=[1, 1])
            == self._IMPOSSIBLE
        )

    def test_10_columns(self):
        assert (
            recover_matrix(
                upper_sum=5, lower_sum=5, column_sum=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            )
            == "0000011111,1111100000"
        )
        assert (
            recover_matrix(
                upper_sum=3, lower_sum=7, column_sum=[1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
            )
            == self._IMPOSSIBLE
        )
        assert (
            recover_matrix(
                upper_sum=3, lower_sum=6, column_sum=[1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
            )
            == "0000001101,1111110000"
        )
        assert (
            recover_matrix(
                upper_sum=3, lower_sum=7, column_sum=[1, 1, 1, 1, 1, 1, 1, 1, 0, 2]
            )
            == "0000001101,1111110001"
        )

    def test_case_1(self):
        e = {"10101,11000", "11001,10100"}
        assert recover_matrix(upper_sum=3, lower_sum=2, column_sum=[2, 1, 1, 0, 1]) in e

    def test_case_2(self):
        assert (
            recover_matrix(upper_sum=2, lower_sum=3, column_sum=[0, 0, 1, 1, 2])
            == self._IMPOSSIBLE
        )

    def test_case_3(self):
        assert (
            recover_matrix(upper_sum=2, lower_sum=2, column_sum=[2, 0, 2, 0])
            == "1010,1010"
        )
