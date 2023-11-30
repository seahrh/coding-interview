import pytest

from sequences.tictactoe import *


class TestTicTacToe:
    def test_when_board_is_too_small_then_raise_error(self):
        with pytest.raises(ValueError):
            has_won(board=[[Piece.EMPTY, Piece.EMPTY], [Piece.CIRCLE, Piece.CIRCLE]])

    def test_given_3x3_board_when_draw_then_has_not_won(self):
        assert not has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
            ]
        )

    def test_given_3x3_board_when_complete_diagonal_down_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
            ]
        )

    def test_given_3x3_board_when_complete_diagonal_up_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
            ]
        )

    def test_given_3x3_board_when_complete_row_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                [Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CIRCLE],
            ]
        )

    def test_given_3x3_board_when_complete_column_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                [Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
            ]
        )

    def test_given_4x4_board_when_draw_then_has_not_won(self):
        assert not has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
            ]
        )

    def test_given_4x4_board_when_complete_diagonal_down_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
            ]
        )

    def test_given_4x4_board_when_complete_diagonal_up_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                [Piece.CROSS, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
            ]
        )

    def test_given_4x4_board_when_complete_row_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CIRCLE, Piece.CIRCLE],
            ]
        )

    def test_given_4x4_board_when_complete_column_then_has_won(self):
        assert has_won(
            board=[
                [Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
            ]
        )
