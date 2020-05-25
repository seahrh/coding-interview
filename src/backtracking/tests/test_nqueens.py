from backtracking.nqueens import *


class TestNQueens:
    def test_queens(self):
        assert queens(1) == [[Position(0, 0)]]
        assert queens(2) == []
        assert queens(3) == []
        assert queens(4) == [
            [
                Position(row=0, col=1),
                Position(row=1, col=3),
                Position(row=2, col=0),
                Position(row=3, col=2),
            ],
            [
                Position(row=0, col=2),
                Position(row=1, col=0),
                Position(row=2, col=3),
                Position(row=3, col=1),
            ],
        ]
        assert queens(5) == [
            [
                Position(row=0, col=0),
                Position(row=1, col=2),
                Position(row=2, col=4),
                Position(row=3, col=1),
                Position(row=4, col=3),
            ],
            [
                Position(row=0, col=0),
                Position(row=1, col=3),
                Position(row=2, col=1),
                Position(row=3, col=4),
                Position(row=4, col=2),
            ],
            [
                Position(row=0, col=1),
                Position(row=1, col=3),
                Position(row=2, col=0),
                Position(row=3, col=2),
                Position(row=4, col=4),
            ],
            [
                Position(row=0, col=1),
                Position(row=1, col=4),
                Position(row=2, col=2),
                Position(row=3, col=0),
                Position(row=4, col=3),
            ],
            [
                Position(row=0, col=2),
                Position(row=1, col=0),
                Position(row=2, col=3),
                Position(row=3, col=1),
                Position(row=4, col=4),
            ],
            [
                Position(row=0, col=2),
                Position(row=1, col=4),
                Position(row=2, col=1),
                Position(row=3, col=3),
                Position(row=4, col=0),
            ],
            [
                Position(row=0, col=3),
                Position(row=1, col=0),
                Position(row=2, col=2),
                Position(row=3, col=4),
                Position(row=4, col=1),
            ],
            [
                Position(row=0, col=3),
                Position(row=1, col=1),
                Position(row=2, col=4),
                Position(row=3, col=2),
                Position(row=4, col=0),
            ],
            [
                Position(row=0, col=4),
                Position(row=1, col=1),
                Position(row=2, col=3),
                Position(row=3, col=0),
                Position(row=4, col=2),
            ],
            [
                Position(row=0, col=4),
                Position(row=1, col=2),
                Position(row=2, col=0),
                Position(row=3, col=3),
                Position(row=4, col=1),
            ],
        ]
