from codi.graphs.image_matching import *


class TestImageMatching:
    def test_case_1(self):
        assert (
            solve(
                g1=[[1, 1, 1], [1, 0, 0], [1, 0, 0]],
                g2=[[1, 1, 1], [1, 0, 0], [1, 0, 1]],
            )
            == 1
        )

    def test_case_2(self):
        assert (
            solve(
                g1=[[1, 1, 1], [1, 0, 1], [1, 0, 0]],
                g2=[[1, 1, 1], [1, 0, 0], [1, 0, 1]],
            )
            == 0
        )

    def test_max_number_of_connected_components(self):
        assert (
            solve(
                g1=[[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]],
                g2=[[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]],
            )
            == 6
        )
        assert (
            solve(
                g1=[[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]],
                g2=[[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 0]],
            )
            == 5
        )

    def test_no_connected_components(self):
        assert (
            solve(
                g1=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                g2=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            )
            == 0
        )
