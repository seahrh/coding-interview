"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.
(10.9, p421)
"""
from collections import namedtuple


def find(matrix, key):
    """
    This algorithm works by elimination. Start from the top right hand corner.
    Every move to the left (--col) eliminates all the elements below the current cell in that column.
    Likewise, every move down eliminates all the elements to the left of the cell in that row.

    This takes O(m+n) time and O(1) space,
    where m and n are number of rows and columns respectively.

    :param matrix: 2d sorted matrix
    :param key:
    :return: index of the element if found, otherwise -1
    """
    if len(matrix) == 0:
        raise ValueError('matrix must not be empty')
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == key:
            return i, j
        if key < matrix[i][j]:
            j -= 1
        else:
            i += 1
    return -1


Cell = namedtuple('Cell', 'row col')


def _in_bounds(matrix, cell):
    return 0 <= cell.row < len(matrix) and 0 <= cell.col < len(matrix[0])


def _is_before(left, right):
    return left.row <= right.row and left.col <= right.col


def _average(min_cell, max_cell):
    return Cell(
        row=int((min_cell.row / 2) + (max_cell.row / 2)),
        col=int((min_cell.col / 2) + (max_cell.col / 2)),
    )


def _partition_and_search(matrix, origin, dest, key, pivot):
    lower_left_origin = Cell(row=pivot.row, col=origin.col)
    lower_left_dest = Cell(row=dest.row, col=pivot.col - 1)
    upper_right_origin = Cell(row=origin.row, col=pivot.col)
    upper_right_dest = Cell(row=pivot.row - 1, col=dest.col)
    res = _binary_search(matrix, lower_left_origin, lower_left_dest, key)
    if res is None:
        res = _binary_search(matrix, upper_right_origin, upper_right_dest, key)
    return res


def _binary_search(matrix, origin, dest, key):
    """Partition the matrix into 4 quadrants and
    recursively search the lower left and upper right quadrants.
    These too will get divided further into quadrants and searched.
    Idea: In a quadrant, the origin is the smallest value and destination is largest.
    e.g.
    [min, ---, ---]
    [---, ---, ---]
    [---, ---, max]
    The key cannot be in the upper left quadrant because key > quadrant destination.
    The key cannot be in the lower right quadrant because key < quadrant origin.
    Since the diagonal is sorted, we can use binary search.
    """
    if not _in_bounds(matrix, origin):
        return None
    if not _in_bounds(matrix, dest):
        return None
    if not _is_before(origin, dest):
        return None
    if matrix[origin.row][origin.col] == key:
        return origin
    # set `lo` and `hi` to be the start and end of the diagonal respectively.
    # since matrix may not be square, end of the diagonal may not equal `hi`
    diagonal_dist = min(dest.row - origin.row, dest.col - origin.col)
    lo = origin
    hi = Cell(row=lo.row + diagonal_dist, col=lo.col + diagonal_dist)
    # binary search on the diagonal, looking for the 1st element > key
    while _is_before(lo, hi):
        mid = _average(lo, hi)
        if key == matrix[mid.row][mid.col]:
            return mid
        if key > matrix[mid.row][mid.col]:
            lo = Cell(row=mid.row + 1, col=mid.col + 1)
        else:
            hi = Cell(row=mid.row - 1, col=mid.col - 1)
    return _partition_and_search(matrix, origin, dest, key, pivot=lo)


def binary_search(matrix, key):
    if len(matrix) == 0:
        raise ValueError('matrix must not be empty')
    return _binary_search(
        matrix=matrix,
        origin=Cell(0, 0),
        dest=Cell(len(matrix) - 1, len(matrix[0]) - 1),
        key=key
    )
