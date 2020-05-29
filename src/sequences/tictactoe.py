"""
Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.
The game is played on a nxn board, where n >= 3
You do not know the last move.
(16.4, p477)
"""
from enum import Enum, auto


class Piece(Enum):
    CROSS = auto()
    CIRCLE = auto()
    EMPTY = auto()


def _has_won(pieces_gen):
    first = None
    for p in pieces_gen:
        if p == Piece.EMPTY:
            return False
        if first is None:
            first = p
            continue
        if first != p:
            return False
    return True


def has_won(board):
    """Check rows, columns and diagonals to see if game is won.
    Time O(n), Space O(1) since generators are used"""
    if len(board) < 3 or len(board[0]) < 3:
        raise ValueError("board dimensions must not be less than 3")
    n = len(board)
    # check diagonals first since there are only two
    diagonal_down = (board[i][i] for i in range(n))  # generator
    if _has_won(diagonal_down):
        return True
    diagonal_up = (board[n - 1 - i][i] for i in range(n))  # generator
    if _has_won(diagonal_up):
        return True
    # check rows
    for i in range(n):
        if _has_won(board[i]):
            return True
    # check cols
    for j in range(n):
        col = (board[i][j] for i in range(n))  # generator
        if _has_won(col):
            return True
    return False
