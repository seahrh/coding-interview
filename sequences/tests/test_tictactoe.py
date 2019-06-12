import unittest
from sequences.tictactoe import *


class TestTicTacToe(unittest.TestCase):
    def test_when_board_is_too_small_then_raise_error(self):
        board = [[Piece.EMPTY, Piece.EMPTY],
                 [Piece.CIRCLE, Piece.CIRCLE]]
        self.assertRaises(ValueError, has_won, board)

    def test_given_3x3_board_when_draw_then_has_not_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), False)

    def test_given_3x3_board_when_complete_diagonal_down_then_has_won(self):
        board = [[Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), True)

    def test_given_3x3_board_when_complete_diagonal_up_then_has_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), True)

    def test_given_3x3_board_when_complete_row_then_has_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), True)

    def test_given_3x3_board_when_complete_column_then_has_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CROSS]
                 ]
        self.assertEqual(has_won(board), True)

    def test_given_4x4_board_when_draw_then_has_not_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), False)

    def test_given_4x4_board_when_complete_diagonal_down_then_has_won(self):
        board = [[Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                 [Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), True)

    def test_given_4x4_board_when_complete_diagonal_up_then_has_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                 [Piece.CROSS, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), True)

    def test_given_4x4_board_when_complete_row_then_has_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CROSS],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CIRCLE, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), True)

    def test_given_4x4_board_when_complete_column_then_has_won(self):
        board = [[Piece.CROSS, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE],
                 [Piece.CIRCLE, Piece.CROSS, Piece.CIRCLE, Piece.CIRCLE]
                 ]
        self.assertEqual(has_won(board), True)


if __name__ == '__main__':
    unittest.main()
