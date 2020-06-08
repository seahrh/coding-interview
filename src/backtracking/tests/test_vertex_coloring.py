from backtracking.vertex_coloring import *


class TestVertexColoring:
    def test_when_graph_has_one_node(self):
        assert vertex_coloring(graph=[[False]], m=1) == {(1,)}

    def test_case_1(self):
        assert vertex_coloring(graph=[[False, True], [True, False]], m=2) == {
            (1, 2),
            (2, 1),
        }

    def test_case_2(self):
        assert vertex_coloring(graph=[[False, True], [True, False]], m=1) == set()

    def test_case_3(self):
        assert vertex_coloring(
            graph=[[False, True, False], [True, False, True], [False, True, False]],
            m=2,
        ) == {(1, 2, 1), (2, 1, 2)}

    def test_case_4(self):
        assert vertex_coloring(
            graph=[[False, True, True], [True, False, False], [True, False, False]],
            m=2,
        ) == {(1, 2, 2), (2, 1, 1)}

    def test_case_5(self):
        assert (
            vertex_coloring(
                graph=[[False, True, True], [True, False, True], [True, True, False]],
                m=2,
            )
            == set()
        )

    def test_case_6(self):
        assert (
            vertex_coloring(
                graph=[
                    [False, True, True, True],
                    [True, False, True, True],
                    [True, True, False, True],
                    [True, True, True, False],
                ],
                m=3,
            )
            == set()
        )

    def test_case_7(self):
        assert vertex_coloring(
            graph=[
                [False, True, True, True],
                [True, False, True, False],
                [True, True, False, True],
                [True, False, True, False],
            ],
            m=3,
        ) == {(1, 2, 3, 2), (2, 1, 3, 1), (3, 1, 2, 1)}
