from codi.graphs.astar import *


class TestAStar:
    MOVES = [
        Position(-1, 0),
        Position(0, -1),
        Position(1, 0),
        Position(0, 1),
    ]  # go UP, DOWN, LEFT, RIGHT

    def test_goal_node_unreachable(self):
        assert (
            search(
                maze=[
                    [0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                ],
                start=Position(0, 0),
                goal=Position(4, 6),
                moves=self.MOVES,
            )
            == []
        )

    def test_example_1(self):
        assert search(
            maze=[
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
            ],
            start=Position(0, 0),
            goal=Position(4, 5),
            moves=self.MOVES,
        ) == [
            Position(0, 0),
            Position(1, 0),
            Position(2, 0),
            Position(3, 0),
            Position(4, 0),
            Position(4, 1),
            Position(4, 2),
            Position(4, 3),
            Position(3, 3),
            Position(3, 4),
            Position(3, 5),
            Position(4, 5),
        ]
